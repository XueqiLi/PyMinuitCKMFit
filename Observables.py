import numpy as np # for calculation

class GeneralCKMSystem:
    def __init__(self,YuMatrix,YdMatrix,numberOfParams,dCPResult=False):
        self.YuMatrix = YuMatrix
        self.YdMatrix = YdMatrix
        self.numberOfParams = numberOfParams
        if dCPResult:
            self.observableName=["s12", "s23", "s13", "mu1", "mu2", "mu3", "md1", "md2", "md3", "dCP"]
        else:
            self.observableName=["s12", "s23", "s13", "mu1", "mu2", "mu3", "md1", "md2", "md3"]
        self.dCPResult = dCPResult

    def GetMixing(self, umatrix):
        s13 = umatrix[0, 2] * np.conjugate(umatrix[0, 2])
        if s13 == 1:
            s12 = 0
            s23 = 0
        else:
            s12 = (umatrix[0, 1] * np.conjugate(umatrix[0, 1])) / (1 - s13)
            s23 = (umatrix[1, 2] * np.conjugate(umatrix[1, 2])) / (1 - s13)
            
        c13 = 1 - s13
        c12 = 1 - s12
        c23 = 1 - s23

        try:
            dCP = (np.angle(
                ((umatrix[0, 0] * umatrix[2, 2] * np.conjugate(umatrix[0, 2]) * np.conjugate(umatrix[2, 0])) /
                (np.sqrt(c12) * np.sqrt(c23) * c13 * np.sqrt(s13)) + 
                np.sqrt(c12) * np.sqrt(c23) * np.sqrt(s13)) / 
                (np.sqrt(s12) * np.sqrt(s23))
                ) / np.pi) 

        except:
            dCP = 0.5 

        return [s12, s23, s13, dCP]
    
    def SVDMixingMass(self, massMatrix):
        L, Eigen, RDagger = np.linalg.svd(massMatrix, full_matrices=True)
        sortedIndices = np.argsort(Eigen)

        EigenSorted = Eigen[sortedIndices]
        LSorted = L[:, sortedIndices]
        RDaggerSorted = RDagger[sortedIndices, :]
        RSorted = RDaggerSorted.T.conjugate()
        
        mass = np.abs(EigenSorted)
        return [mass, RSorted]

    # Calculate Observables
    def Calculate(self, params, printResult=False):
        # params[np.isnan(params)] = 0
        YuMatrixN = np.array(self.YuMatrix(params), dtype=np.cdouble)
        YdMatrixN = np.array(self.YdMatrix(params), dtype=np.cdouble)
        
        if printResult:
            print("YuN: \n",YuMatrixN)
            print("YdN: \n",YdMatrixN)

        Mu, Ru = self.SVDMixingMass(YuMatrixN)
        Md, Rd = self.SVDMixingMass(YdMatrixN)

        if printResult:
            print("Ru: \n",Ru)
            print("Mu: \n",Mu)
            print("Rd: \n",Rd)
            print("Md: \n",Md)

        mu1, mu2, mu3 = Mu
        md1, md2, md3 = Md

        CKM= np.dot(np.conjugate(np.transpose(Ru)), Rd)

        if printResult:
            print("CKM: \n",CKM)

        s12, s23, s13, dCP = self.GetMixing(CKM)

        if self.dCPResult:
            output=np.array([np.real(x) for x in [s12, s23, s13, mu1, mu2, mu3, md1, md2, md3, dCP]], dtype=float)
        else:
            output=np.array([np.real(x) for x in [s12, s23, s13, mu1, mu2, mu3, md1, md2, md3]], dtype=float)
        
        return output
    

    def __call__(self,params, printResult=False):
        return self.Calculate(params, printResult)
    
    def Print(self,params):
        observableResult = self.__call__(params)
        print("Observabls Result:")
        for i in range(len(self.observableName)):
            print(self.observableName[i],": ",observableResult[i])


class CKMSystem(GeneralCKMSystem):
    def __init__(self, YuMatrix, YdMatrix, numberOfParams, dCPResult=False):
        super().__init__(YuMatrix, YdMatrix, numberOfParams, dCPResult)
        if dCPResult:
            self.observableName=["s12", "s23", "s13", "mURmC", "mCRmT", "mDRmS", "mSRmB", "QdCP"]
        else:
            self.observableName=["s12", "s23", "s13", "mURmC", "mCRmT", "mDRmS", "mSRmB"]

    def CalculateCKMResult(self, params, printResult=False):
        if self.dCPResult:
            s12, s23, s13, mu1, mu2, mu3, md1, md2, md3, dCP = self.Calculate(params, printResult)
        else:
            s12, s23, s13, mu1, mu2, mu3, md1, md2, md3 = self.Calculate(params, printResult)
        mURmC = mu1/mu2
        mCRmT = mu2/mu3

        mDRmS = md1/md2
        mSRmB = md2/md3

        if self.dCPResult:
            return [s12, s23, s13, mURmC, mCRmT, mDRmS, mSRmB, dCP]
        else:
            return [s12, s23, s13, mURmC, mCRmT, mDRmS, mSRmB]
    
    def __call__(self,params):
        return self.CalculateCKMResult(params)

class PMNSSystem(GeneralCKMSystem):
    def __init__(self,YuMatrix,YdMatrix,numberOfParams, dCPResult=False):
        super().__init__(YuMatrix, YdMatrix, numberOfParams, dCPResult)
        if dCPResult:
            self.observableName=["s12", "s23", "s13", "m21Rm31", "mERmMu", "mMuRMTau", "dCP"]
        else:
            self.observableName=["s12", "s23", "s13", "m21Rm31", "mERmMu", "mMuRMTau"]

    def CalculatePMNSResult(self, params, printResult=False):
        if self.dCPResult:
            s12, s23, s13, me, mmu, mtau, m1, m2, m3, dCP = self.Calculate(params, printResult)
        else:
            s12, s23, s13, me, mmu, mtau, m1, m2, m3 = self.Calculate(params, printResult)

        m21Rm31 = (m2**2 - m1**2) / (m3**2 - m1**2)
        mERmMu = me/mmu
        mMuRMTau = mmu/mtau

        if self.dCPResult:
            return [s12, s23, s13, m21Rm31, mERmMu, mMuRMTau, dCP]
        else:
            return [s12, s23, s13, m21Rm31, mERmMu, mMuRMTau]
    
    def __call__(self, params):
        return self.CalculatePMNSResult(params)

class PMNSSeeSawSystem(PMNSSystem):
    def __init__(self, YuMatrix, NLMatrix, NNMatrix, numberOfParams, dCPResult=False):
        def YdMatrix(params):
            return -1 * np.dot(np.dot(np.transpose(NLMatrix(params)), np.linalg.inv(NNMatrix(params))), NLMatrix(params))
        super().__init__(YuMatrix, YdMatrix, numberOfParams, dCPResult)

class CMKPMNSSystem:
    def __init__(self, YuMatrix, YdMatrix, YeMatrix, YnuMatrix, numberOfParams, dCPResult=False):
        self.YuMatrix = YuMatrix
        self.YdMatrix = YdMatrix
        self.YeMatrix = YeMatrix
        self.YnuMatrix = YnuMatrix
        self.numberOfParams = numberOfParams
        if dCPResult:
            self.observableName=["Qs12", "Qs23", "Qs13", "mURmC", "mCRmT", "mDRmS", "mSRmB", "QdCP",  "Ls12", "Ls23", "Ls13", "m21Rm31", "mERmMu", "mMuRMTau", "LdCP"]
        else:
            self.observableName=["Qs12", "Qs23", "Qs13", "mURmC", "mCRmT", "mDRmS", "mSRmB", "Ls12", "Ls23", "Ls13", "m21Rm31", "mERmMu", "mMuRMTau"]
        self.QuarkSector=CKMSystem(YuMatrix, YdMatrix, numberOfParams, dCPResult)
        self.LeptonSector=PMNSSystem(YeMatrix, YnuMatrix, numberOfParams, dCPResult)
        self.dCPResult = dCPResult

    def Calculate(self, params, printResult=False):
        QuarkResult = self.QuarkSector.CalculateCKMResult(params, printResult)
        LeptonResult = self.LeptonSector.CalculatePMNSResult(params, printResult)

        return np.concatenate((QuarkResult, LeptonResult))
    
    def __call__(self,params):
        return self.Calculate(params)
    
    def Print(self,params):
        observableResult = self.__call__(params)

        if self.dCPResult:
            QLSplit = 7
        else:
            QLSplit = 8

        print("Observabls Result:")
        print("Quark:")
        for i in range(QLSplit):
            print(self.observableName[i],": ",observableResult[i])
        print("Lepton:")
        for i in range(QLSplit,len(self.observableName)):
            print(self.observableName[i],": ",observableResult[i])

class CKMPMNSSeeSawSystem(CMKPMNSSystem):
    def __init__(self, YuMatrix, YdMatrix, YeMatrix, NLMatrix, NNMatrix, numberOfParams, dCPResult=False):
        def YnuMatrix(params):
            return -1 * np.dot(np.dot(np.transpose(NLMatrix(params)), np.linalg.inv(NNMatrix(params))), NLMatrix(params))
        super().__init__(YuMatrix, YdMatrix, YeMatrix, YnuMatrix, numberOfParams, dCPResult)
