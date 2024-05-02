import numpy as np # for calculation
from iminuit import Minuit # minimize program
tauRange=0.01
class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    ## Bound and scale
    tBounds = [
        (-0.5,-0.5+ tauRange),        # tr
        (np.sqrt(3)/2, np.sqrt(3)/2+tauRange)   #ti
        # (-0.1,0.1),        # tr
        # (0.9, 1.1)   #ti
    ]
    def __init__(self, calResult, expList, divList, modelType="normal", shiftFunction=lambda x: x, upper=20.0):
        self.calResult = calResult
        self.expList=np.asarray(expList)
        self.divList=np.asarray(divList)
        self.shiftFunction = shiftFunction
        self.upper = upper
        self.commonBounds = (-1 * upper,upper)

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