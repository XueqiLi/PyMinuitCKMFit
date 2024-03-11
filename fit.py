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
from CostFunction import *


def main():
    # Arguments
    parser = argparse.ArgumentParser(description='This is a simple script for fitting flavor observables using iMinuit.')
    parser.add_argument('-q', action='store_true', help='fit quark')
    parser.add_argument('-l', action='store_true', help='fit lepton')
    parser.add_argument('-s', action='store_true', help='nuetrino mass is from seesaw')
    parser.add_argument('-NO', action='store_true', help='fit NO lepton')
    parser.add_argument('-IO', action='store_true', help='fit IO lepton')
    parser.add_argument('-cp', action='store_true', help='fit CP phase')
    parser.add_argument('-m', action='store_true', help='modular model')
    parser.add_argument('-three', action='store_true', help='fit for 3 sigma range')
    parser.add_argument('-up', type=float, help='Upper bound value')
    parser.add_argument('-low', type=float, help='Lower bound value')
    parser.add_argument('-mig', type=int, help='number of migrad iteration')
    parser.add_argument('-scan', type=int, help='number of initial points in the begining')
    parser.add_argument('-itr', type=int, help='number of iteration for scan around the best fit')
    parser.add_argument('-f', dest='filePath', type=str, required=True, help='Path to the model file')
    args = parser.parse_args()

    ## Set the agruments
    filePath = args.filePath
    if args.mig:
        migradN = args.mig
    else:
        migradN = 100000
    if args.scan:
        scanN = args.scan
    else:
        scanN = 30
    if args.itr:    
        itrN = args.itr
    else:    
        itrN = 20
    
    lower = args.low if args.low else 0.0
    upper = args.up if args.up else 20.0

    def ShiftFunctionModular(params):
        minScale = lower
        commonParams = params[:-2]
        tParams = params[-2:]
        commonParams = [param + np.sign(param) * minScale for param in commonParams]
        return np.concatenate((commonParams, tParams))

    def ShiftFunction(params):
        minScale = lower
        commonParams = [param + np.sign(param) * minScale for param in params]
        return commonParams

    # Construct the fitting target
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
        
    # Import the model
    directory, moduleName = os.path.split(filePath)
    moduleName = os.path.splitext(moduleName)[0]

    spec = importlib.util.spec_from_file_location(moduleName, filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Construct the observables and cost function
    if quarkswtich:
        if leptonSwitch:
            if seesawSwitch:
                    observables=CKMPMNSSeeSawSystem(module.YuMatrix,module.YdMatrix,module.ELMatrix,module.NLMatrix,module.NNMatrix,module.numberOfParams,dCPResult=cpSwitch)
                    costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=upper)
            else:
                observables=CMKPMNSSystem(module.YuMatrix,module.YdMatrix,module.ELMatrix,module.NLMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=upper)
        else:
            observables=CKMSystem(module.YuMatrix,module.YdMatrix,module.numberOfParams,dCPResult=cpSwitch)
            costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=upper)
    else:
        if leptonSwitch:
            if seesawSwitch:
                observables=PMNSSeeSawSystem(module.ELMatrix,module.NLMatrix,module.NNMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=upper)
            else:
                observables=PMNSSystem(module.ELMatrix,module.NLMatrix,module.numberOfParams,dCPResult=cpSwitch)
                costFunction = CostFunction(observables, ExpList, DivList, modelType = modularType, shiftFunction=shift, upper=upper)
        else:
            print("No fitting target")
            return 1
            
    # Fit!
    # fit on different points
    print("Start fitting...")

    fitResults = []
    for i in range(scanN):
        fit = Minuit(costFunction, costFunction.InitParams()) 
        fit.limits=costFunction.parameterBounds
        fit.strategy=2

        try:
            fit.migrad(migradN)
            fitResults.append(np.asarray(fit.values))
        except:
            continue
    
    fitResult = min(fitResults, key=lambda x: costFunction(x))

    # for the best fit, fit the point around it
    convergingCount = 0
    for i in range(itrN):
        OldResult = fitResult
        fit = Minuit(costFunction,fitResult) 
        fit.limits=costFunction.parameterBounds
        fit.strategy=2
        try:
            fit.migrad(migradN)
        except:
            continue
        fitResultNew=np.asarray(fit.values)
        fitResult=min([fitResultNew,fitResult], key=lambda x: costFunction(x))
        if np.all(OldResult == fitResultNew):
            convergingCount += 1
        if convergingCount > 3:
            break

    
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


