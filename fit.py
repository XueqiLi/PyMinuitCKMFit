import numpy as np # for calculation
import sys # for import model from argument 
import importlib # for import model
from iminuit import Minuit # minimize program
import argparse
import os

# Import fixed data
from ModularForm import *
from ExpData import *

# Import Observable calculation class
from Observables import *

fittingRange = 10
lowerBoundShift = 0.1

class CostFunction:
    errordef = Minuit.LEAST_SQUARES
    ## Bound and scale
    tBounds = [
        (-0.5,-0.4),        # tr
        (np.sqrt(3)/2, 0.95)   #ti
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


def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-q', action='store_true', help='fit quark')
    parser.add_argument('-l', action='store_true', help='fit lepton')
    parser.add_argument('-s', action='store_true', help='nuetrino mass is from seesaw')
    parser.add_argument('-NO', action='store_true', help='fit NO lepton')
    parser.add_argument('-IO', action='store_true', help='fit IO lepton')
    parser.add_argument('-cp', action='store_true', help='fit CP phase')
    parser.add_argument('-m', action='store_true', help='modular model')
    parser.add_argument('-three', action='store_true', help='fit for 3 sigma range')
    parser.add_argument('-up', type=float, required=True, help='Upper bound value')
    parser.add_argument('-low', type=float, required=True, help='Lower bound value')
    parser.add_argument('-f', dest='filePath', type=str, required=True, help='Path to the model file')
    args = parser.parse_args()
    filePath = args.filePath

    def ShiftFunctionModular(params):
        minScale = args.low
        commonParams = params[:-2]
        tParams = params[-2:]
        commonParams = [param + np.sign(param) * minScale for param in commonParams]
        return np.concatenate((commonParams, tParams))

    def ShiftFunction(params):
        minScale = args.low
        commonParams = [param + np.sign(param) * minScale for param in params]
        return commonParams


    ExpList=[]
    DivList=[]
    if args.q: 
        quarkswtich = True
        ExpList=ExpList + quarkCPExpValList
        DivList=DivList + quarkCPDivValList
        cpSwitch = True # for quark, always fit CP phase
    else:
        quarkswtich = False
    if args.l:
        leptonSwitch = True
        if args.s:
            seesawSwitch = True
        else:  
            seesawSwitch = False
        if args.NO: 
            ExpList=ExpList + leptonNOExpValList
            DivList=DivList + leptonNODivValList
        if args.IO:
            ExpList=ExpList + leptonIOExpValList
            DivList=DivList + leptonIODivValList
        if args.cp:
            cpSwitch = True
            ExpList=ExpList + [dCPExp]
            DivList=DivList + [dCPDiv]
        else:
            cpSwitch = False
        if not args.NO and not args.IO:
            print("You must choose NO or IO for lepton")
            return 1
    else:
        leptonSwitch = False
    if args.m:    
        shift = ShiftFunctionModular
        modularType = "modular"
    else:
        shift = ShiftFunction
        modularType = "normal"
    
    if args.three:
        DivList = [x * 3 for x in DivList]
        
    
    directory, moduleName = os.path.split(filePath)
    moduleName = os.path.splitext(moduleName)[0]

    spec = importlib.util.spec_from_file_location(moduleName, filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if quarkswtich:
        if leptonSwitch:
            if seesawSwitch:
                    observables=CKMPMNSSeeSawSystem(module.YuMatrix,module.YdMatrix,module.ELMatrix,module.NLMatrix,module.NNMatrix,module.numberOfParams,dCPResult=cpSwitch)
                    costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=args.up)
            else:
                observables=CMKPMNSSystem(module.YuMatrix,module.YdMatrix,module.ELMatrix,module.NLMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=args.up)
        else:
            observables=CKMSystem(module.YuMatrix,module.YdMatrix,module.numberOfParams,dCPResult=cpSwitch)
            costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=args.up)
    else:
        if leptonSwitch:
            if seesawSwitch:
                observables=PMNSSeeSawSystem(module.ELMatrix,module.NLMatrix,module.NNMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=args.up)
            else:
                observables=PMNSSystem(module.ELMatrix,module.NLMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=args.up)
        else:
            print("No fitting target")
            return 1
            

    print("Start fitting...")

    fit = Minuit(costFunction, costFunction.InitParams()) 
    fit.limits=costFunction.parameterBounds
    fit.strategy=2

    # Fit!
    # fit on different points
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

    # for the best fit, fit the point around it
    convergingCount = 0
    for i in range(20):
        OldResult = fitResult
        fit = Minuit(costFunction,fitResult) 
        fit.limits=costFunction.parameterBounds
        fit.strategy=2
        try:
            fit.migrad(100000)
        except:
            continue
        fitResultNew=np.asarray(fit.values)
        fitResult=min([fitResultNew,fitResult], key=lambda x: costFunction(x))
        if np.all(OldResult == fitResultNew):
            convergingCount += 1
        if convergingCount > 3:
            break

    # print("shifted:")
    # print(ShiftFunction(fitResult))
    
    print("==========================================================")
    print(moduleName)
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


