import numpy as np # for calculation
import scipy
import sys # for import model from argument 
import importlib # for import model
from iminuit import Minuit # minimize program

# Import fixed data
from ModularForm import *
from ExpData import *

class Observables:
    def __init__(self,ELMatrix,NLMatrix,NNMatrix,numberOfParams,shiftFunction=lambda x: x):
        self.ELMatrix = ELMatrix
        self.NLMatrix = NLMatrix
        self.NNMatrix = NNMatrix
        self.numberOfParams = numberOfParams
        self.observableName=["s12", "s23", "s13", "m21Rm31", "mERmMu", "mMuRMTau"]
        self.shiftFunction = shiftFunction

    # Define Function used to calculate observerable
    def GetMassDiff(self, massMatrix):
        eigenvalues = scipy.linalg.eigvals(massMatrix)
        massList = np.abs(eigenvalues)
        massList.sort()

        Dm21 = massList[1] - massList[0]
        Dm31 = massList[2] - massList[0]

        return [Dm21, Dm31]

    def GetMass(self, massMatrix):
        eigenvalues = scipy.linalg.eigvals(massMatrix)
        massList = np.abs(eigenvalues)
        massList.sort()

        me, m_mu, m_tau = np.sort(massList)

        return [me, m_mu, m_tau]

    def GetMixing(self, umatrix):
        s13 = umatrix[0, 2] * np.conjugate(umatrix[0, 2])
        if s13 == 1:
            s12=0
            s23=0
        else:
            s12 = (umatrix[0, 1] * np.conjugate(umatrix[0, 1])) / (1 - s13)
            s23 = (umatrix[1, 2] * np.conjugate(umatrix[1, 2])) / (1 - s13)
        # c13 = 1 - s13
        # c12 = 1 - s12
        # c23 = 1 - s23
        return [s12,s23,s13]

    def DiagHermitian(self, hermitian_matrix):
        # Check if the input matrix is square
        n, m = hermitian_matrix.shape
        if n != m:
            raise ValueError("Input matrix must be square.")

        # Check if the input matrix is Hermitian (equal to its conjugate transpose)
        if not np.allclose(hermitian_matrix, hermitian_matrix.conj().T):
            return ValueError("Input matrix must be Hermition.")

        # Perform eigendecomposition
        eigenvalues, eigenvectors = scipy.linalg.eigh(hermitian_matrix)

        # Sort eigenvalues and eigenvectors in ascending order
        sorted_indices = np.argsort(eigenvalues)
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        # Form the diagonal matrix with sorted eigenvalues on the diagonal
        diagonal_matrix = np.diag(sorted_eigenvalues)

        # The sorted eigenvectors matrix (sorted_eigenvectors) is already a unitary matrix
        unitary_matrix = sorted_eigenvectors

        return unitary_matrix

    # Calculate Observables
    def CalObservables(self, params):
        ELMatrixN = np.array(self.ELMatrix(params), dtype=np.clongdouble)
        NLMatrixN = np.array(self.NLMatrix(params), dtype=np.clongdouble)
        NNMatrixN = np.array(self.NNMatrix(params), dtype=np.clongdouble)

        if scipy.linalg.det(NNMatrixN) == 0:
            Mnu= np.array([[1,0,0],[0,1,0],[0,0,1]], dtype=np.clongdouble)
        else:
            NNMatrixNInverse = scipy.linalg.inv(NNMatrixN)
            Mnu = -1 * np.dot(np.dot(np.transpose(NLMatrixN), NNMatrixNInverse), NLMatrixN)

        MnuDagger = np.conjugate(np.transpose(Mnu))
        ELMatrixNDagger = np.conjugate(np.transpose(ELMatrixN))
        Mnunu = np.dot(MnuDagger, Mnu)
        Mee = np.dot(ELMatrixNDagger, ELMatrixN)
        MeeDiagMatrix = self.DiagHermitian(Mee)
        MnunuDiagMatrix = self.DiagHermitian(Mnunu)
        NUPMNS = np.dot(np.conjugate(np.transpose(MeeDiagMatrix)), MnunuDiagMatrix)

        Dm21, Dm31 = self.GetMassDiff(Mnunu)
        me, m_mu, m_tau = self.GetMass(Mee)
        if Dm31 != 0:
            m21Rm31 = Dm21/Dm31
        else:
            m21Rm31 = 1

        if me == 0:
            mERmMu = 1
            mMuRMTau = 1
        else:
            mERmMu  = np.sqrt(me)/np.sqrt(m_mu)
            mMuRMTau = np.sqrt(m_mu)/np.sqrt(m_tau)

        s12, s23, s13 = self.GetMixing(NUPMNS)

        output=np.array([np.real(x) for x in [s12, s23, s13, m21Rm31, mERmMu, mMuRMTau]], dtype=float)
        return output
    
    def __call__(self,params):
        return self.CalObservables(self.shiftFunction(params))
    
    def print(self,params):
        observableResult = self.CalObservables(self.shiftFunction(params))
        print("Observabls Result:")
        for i in range(6):
            print(self.observableName[i],": ",observableResult[i])

class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    ## Bound and scale
    commonBounds = (-20,20)
    tBounds = [
        (-0.5,-0.4),        # tr
        (np.sqrt(3)/2, 0.95)   #ti
    ]
    def __init__(self, calResult, expList, divList):
        self.calResult = calResult
        self.expList=np.asarray(expList)
        self.divList=np.asarray(divList)

        self.numberOfParams=calResult.numberOfParams
        self.parameterBoundsWithoutT = [self.commonBounds for i in range(self.numberOfParams)]
        self.parameterBounds = self.parameterBoundsWithoutT + self.tBounds
    
    def __call__(self,params):
        result=self.Prediction(params)
        return np.sum((self.expList-result) ** 2 / (self.divList ** 2))
    
    def SigmaAway(self,params):
        result=self.Prediction(params)
        return np.asarray((self.expList-result) ** 2 / (self.divList ** 2))
    
    def Prediction(self,params):
        return self.calResult(params)
    
    def InitParams(self):
        # Use this for use middle points for the init points
        # return [(bound[1]-bound[0])/2 for bound in parameterBounds]
        return [np.random.uniform(low=bound[0], high=bound[1]) for bound in self.parameterBounds]
    
    def InitParamsMid(self):
        # Use this for use middle points for the init points
        return [(bound[1]-bound[0])/2 for bound in self.parameterBounds]
    
    def StepSize(self):
        stepScale = 1/1000
        parameterRanges = np.asarray(self.parameterBounds)[:, 1] - np.asarray(self.parameterBounds)[:, 0]
        return parameterRanges * stepScale
    
    def print(self,params):
        chiSqr=self.__call__(params)
        sigmaAway=self.SigmaAway(params)
        observableName=self.calResult.observableName
        print("Fit Result:")
        print(params)
        print("----------------------------------------------------------")
        print("Sigma Away:")
        for i in range(6):
            print(observableName[i],": ",sigmaAway[i])
        print("----------------------------------------------------------")

        print("total chi-sqr: ",chiSqr)

def ShiftFunction(params):
    minScale = 0.08
    commonParams = params[:-2]
    tParams = params[-2:]
    commonParams = [param + np.sign(param) * minScale for param in commonParams]
    return np.concatenate((commonParams, tParams))

def main():
    # Import Model from agrument of file
    # from model import *
    modelName = sys.argv[1]
    modelModule = importlib.import_module(modelName)
    # globals().update(vars(modelModule))

    observables=Observables(modelModule.ELMatrix,modelModule.NLMatrix,modelModule.NNMatrix,modelModule.numberOfParams,shiftFunction=ShiftFunction)
    costFunction = CostFunction(observables,expValList,divValList)

    fit = Minuit(costFunction, costFunction.InitParams()) 
    fit.limits=costFunction.parameterBounds
    fit.strategy=2

    #Fit!
    fit.scan(70000)
    print("scan done, current chi-sqr=",costFunction(np.asarray(fit.values)))

    fit.simplex()
    print("simplex done, current chi-sqr=",costFunction(np.asarray(fit.values)))

    fit.migrad(None,500)
    fitResult1=fit.values
    fitChi1=costFunction(fitResult1)
    # fit.reset()
    # fit.values=np.asarray(fitResult1)
    fit.migrad(None,500)
    fitResult2=np.asarray(fit.values)
    fitChi2=costFunction(fitResult2)
    i = 1

    while ((fitChi1 - fitChi2) ** 2 > 0.001) and i < 500:
        if fitChi1 < fitChi2:
            fitResult1=fitResult1
        else:
            firResult1=fitResult2
        fitChi1=costFunction(fitResult1)
        # fit.reset()
        # fit.values=np.asarray(fitResult1)
        fit.migrad(None,5)
        fitResult2=fit.values
        fitChi2=costFunction(fitResult2)
    print(i,"loop is done")
    # print result

    fitResult=np.asarray(fit.values)

    print("shifted:")
    print(ShiftFunction(fitResult))
    print("==========================================================")
    costFunction.print(fitResult)
    print("Numer of Params: ",costFunction.calResult.numberOfParams + 2)
    print("===============----------------------------===============")
    costFunction.calResult.print(fitResult)
    print("==========================================================")

    return 0

if __name__ == "__main__":
    sys.exit(main())


