import numpy as np
def householder_reflection(A):
    
    vec = np.squeeze(A)
    norm = np.linalg.norm(vec)

    #print(norm)
    #v_norm = np.linalg.norm(v)
    if norm == 0:
        return np.eye(len(v)), v
    else:
        new = np.zeros(vec.shape)
        new[0] = 1 * np.sign(A[0][0]) * norm
        
        u = vec - new
        
        
        #return
        u = u/np.linalg.norm(u)*np.sqrt(2)
        v = u/u[0]
        v = v.reshape((-1,1))
        s = np.array([[u[0]*u[0]]])

        vsvT = s*v@v.T
        Q = np.eye(vsvT.shape[0]) - vsvT

        R = Q.T@A

        return v,s,np.array([[norm]])
            

def recursive_qr_factorization(A):
    #Add docstring
    m, n = A.shape
    if n == 1:
        return householder_reflection(A)
    else:
        mid = n//2
        A1 = A[:, :mid]
        A2 = A[:, mid:]

        
        

        #print(A2.shape,"emek")
        Y1,T1,R1 = recursive_qr_factorization(A1.copy())
        #print("\n\n\n", Y1.shape,T1.shape,R1.shape ,"\n\n\n")
        Y1T1Y1_T = Y1@T1@Y1.T
        
        Q1 = np.eye(Y1T1Y1_T.shape[0]) -  Y1T1Y1_T
        

        A2 = Q1.T@A2
        
        A2_part = A2[mid:]

        Y2_hat,T2,R2 = recursive_qr_factorization(A2_part.copy())
        
        
        Y2 = np.block([[np.zeros((m - Y2_hat.shape[0],Y2_hat.shape[1] ))], [Y2_hat]])
        #print(T1.shape,Y1.T.shape,Y2.shape,T2.shape)

        T3 = -T1@(Y1.T@Y2)@T2
        #print("     ", R1.shape,A2[:mid].shape)
        
        Y = np.block([[Y1,Y2]])
        
        T = np.block([[T1,T3],[np.zeros((T2.shape[0],T1.shape[1])),T2]])

        R = np.block([[R1,A2[:mid]],[np.zeros((R2.shape[0],R1.shape[1])),R2]])
        
        
        return Y,T,R
        
        
        
        
       