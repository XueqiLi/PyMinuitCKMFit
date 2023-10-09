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

# Import calculating observerable
from CalObs import *

class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    def __init__(self, calResult, expList, divList):
        self.calResult = calResult
        self.expList=np.asarray(expList)
        self.divList=np.asarray(divList)
    
    def __call__(self,params):
        result=self.prediction(params)
        return np.sum((self.expList-result) ** 2 / (self.divList ** 2))
    
    def prediction(self,params):
        return self.calResult(params)

costFunction = CostFunction(CalObservables,expValList,divValList)
# Fit

## Bound and merge
commonBounds = (-10,10)
tBounds = [
    (-0.5,-0.4),        # tr
    (np.sqrt(3)/2, 0.95)   #ti
]

parameterBoundsWithoutT = [commonBounds for i in range(numberOfParams)]
parameterBounds = np.array(parameterBoundsWithoutT + tBounds)

parameterRanges = parameterBounds[:, 1] - parameterBounds[:, 0]

sizeScale = 1/10000
mergeScale = 1/100000

mergeThreshold = parameterRanges * mergeScale

def are_parameters_close(params1, params2, threshold):
    params1 = np.array(params1)
    params2 = np.array(params2)
    return np.all(np.abs(params1 - params2) < threshold)

## Actual Fit

def fit():
    initParams = [np.random.uniform(low=bound[0], high=bound[1]) for bound in parameterBounds]
    Minuit(CostFunction, initParams) 
    return 0