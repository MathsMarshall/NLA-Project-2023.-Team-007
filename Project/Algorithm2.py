import numpy as np
from scipy.linalg import cholesky, lu

def block_cholesky_lu_qr_factorization(A):
    '''
    
    '''
    At_square = A.T @ A  # Compute ATA
    R_square = cholesky(At_square)  # Cholesky factor of ATA
    
    A_square = A[:R_square.shape[0]]  # Consider square part of A
    
    
    A_square_minus_R = A_square - R_square  # Compute A□ - R□
    P, L, U = lu(A_square_minus_R)  # LU factors of A□ - R□
    
    
    # This matrix has to have a the permutation matrix as I
    #print(P)
    R_inverse = np.linalg.inv(R_square)
    #print(A_square.shape,R_square.shape,L.shape)
    L_inverse = np.linalg.inv(L)
    #S = -1 * (U @ R_inverse) @ L_inverse.T  # Compute S
    S = -1 * (R_inverse@L_inverse.T)@np.linalg.inv(U.T)
   
    Ar = A[R_square.shape[0]:]  # Taking the rectangular part of A
    #V = np.hstack((L, Ar @ np.linalg.inv(U)))  # Compute V
    #V = np.block([[L],[Ar@np.linalg.inv(U)]])
    V = np.block([[A_square_minus_R],[Ar]])

    return V, S, R_square
