import numpy as np # for calculation
import scipy
import sys # for import model from argument 
import importlib # for import model
from iminuit import Minuit # minimize program

# Import fixed data
from ModularForm import *
from ExpData import *

# Import Observable calculation class
from Observables import *

class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    ## Bound and scale
    commonBounds = (-20,20)
    tBounds = [
        (-0.5,-0.4),        # tr
        (np.sqrt(3)/2, 0.95)   #ti
    ]
    def __init__(self, calResult, expList, divList, modelType="normal", shiftFunction=lambda x: x):
        self.calResult = calResult
        self.expList=np.asarray(expList)
        self.divList=np.asarray(divList)
        self.shiftFunction = shiftFunction

        self.numberOfParams=calResult.numberOfParams
        if modelType == "normal":
            self.parameterBounds = [self.commonBounds for i in range(self.numberOfParams)]
        elif modelType == "modular":
            self.parameterBoundsWithoutT = [self.commonBounds for i in range(self.numberOfParams)]
            self.parameterBounds = self.parameterBoundsWithoutT + self.tBounds
    
    def __call__(self,params):
        result=self.Prediction(params)
        return np.sum((self.expList-result) ** 2 / (self.divList ** 2))
    
    def SigmaAway(self,params):
        result=self.Prediction(params)
        return np.asarray((self.expList-result) ** 2 / (self.divList ** 2))
    
    def Prediction(self,params):
        return self.calResult(self.shiftFunction(params))
    
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
    
    def Print(self,params):
        chiSqr=self.__call__(params)
        sigmaAway=self.SigmaAway(params)
        observableName=self.calResult.observableName
        print("Fit Result:")
        print(self.shiftFunction(params))
        print("----------------------------------------------------------")
        print("Sigma Away:")
        for i in range(len(self.expList)):
            print(observableName[i],": ",sigmaAway[i])
        print("----------------------------------------------------------")

        print("total chi-sqr: ",chiSqr)

# def ShiftFunction(params):
#     minScale = 0.08
#     commonParams = params[:-2]
#     tParams = params[-2:]
#     commonParams = [param + np.sign(param) * minScale for param in commonParams]
#     return np.concatenate((commonParams, tParams))
        
def ShiftFunction(params):
    minScale = 0.08
    commonParams = params[:-2]
    tParams = params[-2:]
    commonParams = [param + np.sign(param) * minScale for param in commonParams]
    return np.concatenate((commonParams, tParams))

def main():
    print("Start fitting...")
    # Import Model from agrument of file
    # from model import *
    modelName = sys.argv[1]
    modelModule = importlib.import_module(modelName)

    # waiting to be done for the modular switch
    # globals().update(vars(modelModule))
    
    # observables=CKMPMNSSeeSawSystem(modelModule.YuMatrix,modelModule.YdMatrix,modelModule.ELMatrix,modelModule.NLMatrix,modelModule.NNMatrix,modelModule.numberOfParams)
    # costFunction = CostFunction(observables,expValList,divValList)

    observables=PMNSSeeSawSystem(modelModule.ELMatrix,modelModule.NLMatrix,modelModule.NNMatrix,modelModule.numberOfParams, dCPResult=True)
    costFunction = CostFunction(observables,leptonCPExpValList,leptonCPDivValList,modelType = "modular",shiftFunction=ShiftFunction)

    fit = Minuit(costFunction, costFunction.InitParams()) 
    fit.limits=costFunction.parameterBounds
    fit.strategy=2

    # fit.scan(100000000)
    # print("scan done, current chi-sqr=",costFunction(np.asarray(fit.values)))

    # fit.simplex()
    # print("simplex done, current chi-sqr=",costFunction(np.asarray(fit.values)))

    # fit.migrad(None,500)

    # fitResult = np.asarray(fit.values)

    # Fit!
    fitResults = []
    for i in range(30):
        fit = Minuit(costFunction, costFunction.InitParams()) 
        fit.limits=costFunction.parameterBounds
        fit.strategy=2

        try:
            fit.migrad(100000)
            fitResults.append(np.asarray(fit.values))
        except:
            continue
    
    fitResult = min(fitResults, key=lambda x: costFunction(x))

    # print("shifted:")
    # print(ShiftFunction(fitResult))
    
    print("==========================================================")
    print(modelName)
    print("Number of parameters:")
    print(costFunction.numberOfParams)
    print("==========================================================")
    costFunction.Print(fitResult)
    print("===============----------------------------===============")
    costFunction.calResult.Print(ShiftFunction(fitResult))
    print("==========================================================")

    return 0

if __name__ == "__main__":
    sys.exit(main())


