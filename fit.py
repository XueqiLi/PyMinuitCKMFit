import numpy as np # for calculation
import sys # for import model from argument 
import importlib # for import model
from iminuit import Minuit # minimize program

# Import fixed data
from ModularForm import *
from ExpData import *

# Import Model from agrument of file
# from model import *
modelName = sys.argv[1]
modelModule = importlib.import_module(modelName)
globals().update(vars(modelModule))

class Observables:
    def __init__(self,ELMatrix,NLMatrix,NNMatrix):
        self.ELMatrix = ELMatrix
        self.NLMatrix = NLMatrix
        self.NNMatrix = NNMatrix

    # Define Function used to calculate observerable
    def GetMassDiff(self, massMatrix):
        eigenvalues = np.linalg.eigvals(massMatrix)
        massList = np.abs(eigenvalues)
        massList.sort()

        Dm21 = massList[1] - massList[0]
        Dm31 = massList[2] - massList[0]

        return [Dm21, Dm31]

    def GetMass(self, massMatrix):
        eigenvalues = np.linalg.eigvals(massMatrix)
        massList = np.abs(eigenvalues)
        massList.sort()

        me, m_mu, m_tau = np.sort(massList)

        return [me, m_mu, m_tau]

    def GetMixing(self, umatrix):
        s13 = umatrix[0, 2] * np.conjugate(umatrix[0, 2])
        s12 = (umatrix[0, 1] * np.conjugate(umatrix[0, 1])) / (1 - s13)
        s23 = (umatrix[1, 2] * np.conjugate(umatrix[1, 2])) / (1 - s13)
        c13 = 1 - s13
        c12 = 1 - s12
        c23 = 1 - s23
        return [s12,s23,s13]

    def DiagHermitian(self, hermitian_matrix):
        # Check if the input matrix is square
        n, m = hermitian_matrix.shape
        if n != m:
            raise ValueError("Input matrix must be square.")

        # Check if the input matrix is Hermitian (equal to its conjugate transpose)
        if not np.allclose(hermitian_matrix, hermitian_matrix.conj().T):
            print(hermitian_matrix)
            raise ValueError("Input matrix must be Hermitian.")

        # Perform eigendecomposition
        eigenvalues, eigenvectors = np.linalg.eigh(hermitian_matrix)

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
        ELMatrixN = np.array(self.ELMatrix(params))
        NLMatrixN = np.array(self.NLMatrix(params))
        NNMatrixN = np.array(self.NNMatrix(params))
        Mnu = -(np.transpose(NLMatrixN) @ np.linalg.inv(NNMatrixN) @ NLMatrixN)
        MnuDagger = Mnu.conj().T
        ELMatrixNDagger = ELMatrixN.conj().T
        Mnunu = MnuDagger @ Mnu
        Mee = ELMatrixNDagger @ ELMatrixN
        MeeDiagMatrix = self.DiagHermitian(Mee)
        MnunuDiagMatrix = self.DiagHermitian(Mnunu)
        NUPMNS = np.dot(np.conj(MeeDiagMatrix.T), MnunuDiagMatrix)

        Dm21, Dm31 = self.GetMassDiff(Mnunu)
        me, m_mu, m_tau = self.GetMass(Mee)
        m21Rm31 = Dm21/Dm31
        mERmMu  = np.sqrt(me)/np.sqrt(m_mu)
        mMuRMTau = np.sqrt(m_mu)/np.sqrt(m_tau)
        s12, s23, s13 = self.GetMixing(NUPMNS)

        output=np.array([np.real(x) for x in [s12, s23, s13, m21Rm31, mERmMu, mMuRMTau]], dtype=float)
        return output
    def __call__(self,params):
        return self.CalObservables(params)

observables=Observables(ELMatrix,NLMatrix,NNMatrix)

class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    def __init__(self, calResult, expList, divList):
        self.calResult = calResult
        self.expList=np.asarray(expList)
        self.divList=np.asarray(divList)
    
    def __call__(self,params):
        result=self.Prediction(params)
        return np.sum((self.expList-result) ** 2 / (self.divList ** 2))
    
    def SigmaAway(self,params):
        result=self.Prediction(params)
        return np.asarray((self.expList-result) ** 2 / (self.divList ** 2))
    
    def Prediction(self,params):
        return self.calResult(params)

costFunction = CostFunction(observables,expValList,divValList)
# Fit

## Bound and scale
commonBounds = (-20,20)
tBounds = [
    (-0.5,-0.4),        # tr
    (np.sqrt(3)/2, 0.95)   #ti
]

parameterBoundsWithoutT = [commonBounds for i in range(numberOfParams)]
parameterBounds = parameterBoundsWithoutT + tBounds

stepScale = 1/1000
parameterRanges = np.asarray(parameterBounds)[:, 1] - np.asarray(parameterBounds)[:, 0]
stepSize = parameterRanges * stepScale

## Actual Fit

# Random init points
initParams = [np.random.uniform(low=bound[0], high=bound[1]) for bound in parameterBounds]

# Use this for use middle points for the init points
# initParams = [(bound[1]-bound[0])/2 for bound in parameterBounds]

fit = Minuit(costFunction, initParams) 
fit.limits=parameterBounds
# fit.errors=stepSize


fit.scan(70000)
print("scan done, current chi-sqr=",costFunction(np.asarray(fit.values)))

fit.simplex()
print("simplex done, current chi-sqr=",costFunction(np.asarray(fit.values)))

# fit.migrad(None,10000)
for i in range(10):
    fit.migrad(2000,2000)
    print("migrad done", (i + 1) * 2000, "times, current chi-sqr:",costFunction(np.asarray(fit.values)))

# recording result
fitResult=np.asarray(fit.values)
observableResult=observables(fitResult)
chiSqr=costFunction(fitResult)
sigmaAway=costFunction.SigmaAway(fitResult)

# Print
print("==========================================================")
print("\n")
print("Fit Result")
print(fitResult)
print("\n")
print("Observabls Result:")
observableName=["s12", "s23", "s13", "m21Rm31", "mERmMu", "mMuRMTau"]
for i in range(6):
    print(observableName[i],": ",observableResult[i])
print("\n")

print("Sigma Away:")
for i in range(6):
    print(observableName[i],": ",sigmaAway[i])
print("\n")

print("total chi-sqr: ",chiSqr)