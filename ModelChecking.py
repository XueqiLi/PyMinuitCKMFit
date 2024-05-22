import numpy as np

def ModelCheckCalculation(NNMatrix, NLMatrix, ELMatrix, param):
    # Replace the last two numbers of param with [0, 1]
    param[-2:] = [-0.5, np.sqrt(3)/2]

    try:
        # Evaluate the determinant of NNMatrix at param
        detNN = np.linalg.det(NNMatrix(param))

        # Evaluate the determinant of NLMatrix at param
        detNL = np.linalg.det(NLMatrix(param))

        # Round the values close to zero to zero
        if abs(detNN) < 1e-10:
            detNN = 0
        if abs(detNL) < 1e-10:
            detNL = 0
    except :
        # Handle the case when the determinant calculation fails
        pass
    return [detNN, detNL]

def ModelCheck(NNMatrix, NLMatrix, ELMatrix, param):
    result = ModelCheckCalculation(NNMatrix, NLMatrix, ELMatrix, param)
    return result[0] != 0 and result[1] != 0

def ModelCheckPrint(NNMatrix, NLMatrix, ELMatrix, param):
    result = ModelCheckCalculation(NNMatrix, NLMatrix, ELMatrix, param)
    print("det NNMatrix =", result[0])
    print("det NLMatrix =", result[1])
    