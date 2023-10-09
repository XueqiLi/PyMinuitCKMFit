import numpy as np

from ModularForm import *

# Define Function used to calculate observerable
def GetMassDiff(massMatrix):
    eigenvalues = np.linalg.eigvals(massMatrix)
    massList = np.abs(eigenvalues)
    massList.sort()

    Dm21 = massList[1] - massList[0]
    Dm31 = massList[2] - massList[0]

    return [Dm21, Dm31]

def GetMass(massMatrix):
    eigenvalues = np.linalg.eigvals(massMatrix)
    massList = np.abs(eigenvalues)
    massList.sort()

    me, m_mu, m_tau = np.sort(massList)

    return [me, m_mu, m_tau]

def GetMixing(umatrix):
    s13 = umatrix[0, 2] * np.conjugate(umatrix[0, 2])
    s12 = (umatrix[0, 1] * np.conjugate(umatrix[0, 1])) / (1 - s13)
    s23 = (umatrix[1, 2] * np.conjugate(umatrix[1, 2])) / (1 - s13)
    c13 = 1 - s13
    c12 = 1 - s12
    c23 = 1 - s23
    return [s12,s23,s13]

def DiagHermitian(hermitian_matrix):
    # Check if the input matrix is square
    n, m = hermitian_matrix.shape
    if n != m:
        raise ValueError("Input matrix must be square.")

    # Check if the input matrix is Hermitian (equal to its conjugate transpose)
    if not np.allclose(hermitian_matrix, hermitian_matrix.conj().T):
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
def CalObservables(params):
    ELMatrixN = np.array(ELMatrix(params))
    NLMatrixN = np.array(NLMatrix(params))
    NNMatrixN = np.array(NNMatrix(params))
    Mnu = -(np.transpose(NLMatrixN) @ np.linalg.inv(NNMatrixN) @ NLMatrixN)
    MnuDagger = Mnu.conj().T
    ELMatrixNDagger = ELMatrixN.conj().T
    Mnunu = MnuDagger @ Mnu
    Mee = ELMatrixNDagger @ ELMatrixN
    MeeDiagMatrix = DiagHermitian(Mee)
    MnunuDiagMatrix = DiagHermitian(Mnunu)
    NUPMNS = np.dot(np.conj(MeeDiagMatrix.T), MnunuDiagMatrix)

    Dm21, Dm31 = GetMassDiff(Mnunu)
    me, m_mu, m_tau = GetMass(Mee)
    m21Rm31 = Dm21/Dm31
    mERmMu  = np.sqrt(me)/np.sqrt(m_mu)
    mMuRMTau = np.sqrt(m_mu)/np.sqrt(m_tau)
    s12, s23, s13 = GetMixing(NUPMNS)

    output=np.array([np.real(x) for x in [s12, s23, s13, m21Rm31, mERmMu, mMuRMTau]], dtype=float)
    return output