import numpy as np
from scipy.linalg import cholesky, lu

def block_cholesky_lu_qr_factorization(A : np.array) -> tuple : 
    '''
    Computes the Cholesky factorization of a Matrrix A and returns
    The necessary block matrices to build it back up


    For the function to work properly, the matrix should be tall rectangular with FULL RANK
    ie the number of rows (m) should be greater than the number of columns(n)

    Also, as per the research paper, the LU decomposition used below MUST exist(ie
    the permutation matrix should be the identity)
    '''
    At_square = A.T @ A  # Compute ATA
    R_square = cholesky(At_square)  # Cholesky factor of ATA
    
    A_square = A[:R_square.shape[0]]  # Consider square part of A
    
    
    A_square_minus_R = A_square - R_square  # Compute A□ - R□
    P, L, U = lu(A_square_minus_R)  # LU factors of A□ - R□
    # This matrix has to have a the permutation matrix as I

    

    R_inverse = np.linalg.inv(R_square)
    L_inverse = np.linalg.inv(L)
    S = -1 * (R_inverse@L_inverse.T)@np.linalg.inv(U.T)
    Ar = A[R_square.shape[0]:]  # Taking the rectangular part of A
    V = np.block([[A_square_minus_R],[Ar]])

    return V, S, R_square
