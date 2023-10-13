import numpy as np
import multiprocessing
import concurrent.futures
from tqdm import tqdm
from scipy.optimize import minimize
import sys
import importlib

from ModularForm import *
from ExpData import *

# Import Model
# from model import *
modelName = sys.argv[1]
modelModule = importlib.import_module(modelName)
globals().update(vars(modelModule))


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

def CostFunction(params):
    s12, s23, s13, m21Rm31, mERmMu, mMuRMTau = CalObservables(params)

    diff_s12 = (s12Exp - s12) / s12Div
    diff_s23 = (s23Exp - s23) / s23Div
    diff_s13 = (s13Exp - s13) / s13Div
    diff_m21Rm31 = (m21Rm31Exp - m21Rm31) / m21Rm31Div
    diff_mERmMu = (mERmMuExp - mERmMu) / mERmMuDiv
    diff_mMuRMTau = (mMuRMTauExp - mMuRMTau) / mMuRMTauDiv

    chiSqr = (
        diff_s12 ** 2
        + diff_s23 ** 2
        + diff_s13 ** 2
        + diff_m21Rm31 ** 2
        + diff_mERmMu ** 2
        + diff_mMuRMTau ** 2
    )

    return chiSqr
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

def monte_carlo_fit_subset(start, end, progress_bar=None, best_fit_params_list=None, best_fit_chi_square_list=None):

    if best_fit_params_list is None:
        best_fit_params_list = []
    if best_fit_chi_square_list is None:
        best_fit_chi_square_list = []

    num_past_best_fit = 10
    lowest_best_fit_chi_square = float('inf')


    for _ in range(start, end):
        # Generate random parameter values using the Dirichlet distribution
        # to focus more on unexplored regions and best-fit points
        if len(best_fit_params_list) > 0 and np.random.random() < 0.5:
            idx = np.random.randint(len(best_fit_params_list))

            # Calculate the scale as one-thousandth of the parameter bounds
            scale = np.abs((parameterBounds[:, 1] - parameterBounds[:, 0]) * (sizeScale))

            # Generate random parameter values around the selected best fit point
            params = np.random.normal(best_fit_params_list[idx], scale=scale)
            params = np.clip(params, parameterBounds[:, 0], parameterBounds[:, 1])

        else:
            # Convert the parameters back to a list
            params = [np.random.uniform(low=bound[0], high=bound[1]) for bound in parameterBounds]

        predictions = CalObservables(params)

        current_chi_square = CostFunction(params)

        # Initialize a variable to track whether a merge occurred
        merge_occurred = False

        for stored_params in best_fit_params_list:
            if are_parameters_close(params, stored_params, mergeThreshold):
                # Compare current chi-square with the stored best fit chi-square
                stored_chi_square = best_fit_chi_square_list[idx]
                if current_chi_square < stored_chi_square:
                    # Keep the newly generated parameters
                    best_fit_params_list[idx] = params
                    best_fit_chi_square_list[idx] = current_chi_square
                    merge_occurred = True  
                break

        # If a merge occurred, skip updating the best-fit list if it is already full
        if merge_occurred:
            continue 

        # Update the best-fit list with the current parameter set if it is one of the top 10 best fits
        if len(best_fit_params_list) < num_past_best_fit:
            best_fit_params_list.append(params)
            best_fit_chi_square_list.append(current_chi_square)
        else:
            min_index = np.argmin(best_fit_chi_square_list)
            if current_chi_square < best_fit_chi_square_list[min_index]:
                best_fit_params_list[min_index] = params
                best_fit_chi_square_list[min_index] = current_chi_square

        # Update the lowest_best_fit_chi_square if the current best fit is better
        if current_chi_square < lowest_best_fit_chi_square:
            lowest_best_fit_chi_square = current_chi_square

        # Update the progress bar for the current core with the lowest best-fit chi-square value so far
        if progress_bar:
            best_fit_chi_square_for_progress = np.sqrt(min(best_fit_chi_square_list))
            progress_bar.set_postfix({"CS": f"{best_fit_chi_square_for_progress:.1f}"}, refresh=True)
            progress_bar.update(1)

    # Find the best fit parameters and their chi-square value
    best_index = np.argmin(best_fit_chi_square_list)
    best_fit_params = best_fit_params_list[best_index]
    best_fit_chi_square = best_fit_chi_square_list[best_index]

    return best_fit_params, best_fit_chi_square

## Monte Carlo simulation
def monte_carlo_fit_with_progress(num_trials):
    num_processes = multiprocessing.cpu_count()
    trials_per_process = num_trials // num_processes

    # Create a thread pool executor
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_processes) as executor:
        # Create a list of progress bars for each core
        progress_bars = [tqdm(total=trials_per_process, desc=f"Core {i+1}", ncols=100) for i in range(num_processes)]
        futures = [executor.submit(monte_carlo_fit_subset, i * trials_per_process, (i + 1) * trials_per_process, progress_bars[i]) for i in range(num_processes)]
        
        # Display the progress bars for each core while awaiting completion of all futures
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Wait for the future to complete

    # Close all progress bars
    for progress_bar in progress_bars:
        progress_bar.close()

    # Find the best fit parameters and chi-square from all processes
    best_fit_params = None
    best_fit_chi_square = float('inf')
    for future in futures:
        params, chi_square_value = future.result()
        if chi_square_value < best_fit_chi_square:
            best_fit_params = params
            best_fit_chi_square = chi_square_value

    return best_fit_params, best_fit_chi_square

# Actual Program


# Number of trials for the Monte Carlo simulation
# num_trials = 1000000*2 * 4
num_trials = 1000000*3

# Perform the Monte Carlo fit with progress bars for each core
best_fit_params, best_fit_chi_square = monte_carlo_fit_with_progress(num_trials)

# Calculate the Best Fit Values and Sigma away
best_fit_predictions = CalObservables(best_fit_params)
sigma_away = np.sqrt(best_fit_chi_square)

# Output results
print("=== Best Fit Parameters ===")

print(f"\n")
print(f"{best_fit_params}")

print("\n=== Best Fit Values ===")
print(f"s12: {best_fit_predictions[0]:.3f}")
print(f"s23: {best_fit_predictions[1]:.3f}")
print(f"s13: {best_fit_predictions[2]:.5f}")
print(f"m21Rm31: {best_fit_predictions[3]:.5f}")
print(f"mERmMu: {best_fit_predictions[4]:.4f}")
print(f"mMuRMTau: {best_fit_predictions[5]:.3f}")

print("\n=== Sigma Away ===")
print(f"Total: {sigma_away}")

# Given observed values and uncertainties
observed_values = [0.303, 0.572, 0.02225, 0.02956, 0.0048, 0.059]
uncertainties = [0.012, 0.016, 0.00059, 0.00084, 0.0002, 0.002]

# Calculate the chi-square for each observed quantity
chi_squares = [((observed - prediction) / uncertainty) ** 2 for observed, prediction, uncertainty in zip(observed_values, best_fit_predictions, uncertainties)]

# Calculate the sigma away for each observed quantity
sigma_away = [np.sqrt(chi_square) for chi_square in chi_squares]

print(f"s12: {sigma_away[0]:.3f}")
print(f"s23: {sigma_away[1]:.3f}")
print(f"s13: {sigma_away[2]:.5f}")
print(f"m21Rm31: {sigma_away[3]:.5f}")
print(f"mERmMu: {sigma_away[4]:.4f}")
print(f"mMuRMTau: {sigma_away[5]:.3f}")
