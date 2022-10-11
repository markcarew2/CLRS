import numpy as np
import random

np.random.seed(3)
size = 256

A = np.round(np.random.rand(size,size) * 15)

B = np.round(np.random.rand(size,size) * 15)

ans = np.matmul(A,B)

C = np.zeros((size, size))

def MatMulRec(A,B,C, n):
    if n == 1:
        C[0,0] = C[0,0] + A[0,0] * B[0,0]
        return
    
    n = int(n/2)
    MatMulRec(A[:n,:n],B[:n,:n],C[:n,:n], n)
    MatMulRec(A[:n,n:],B[n:,:n],C[:n,:n], n)
    MatMulRec(A[:n,:n],B[:n,n:],C[:n,n:], n)
    MatMulRec(A[:n,n:],B[n:,n:],C[:n,n:], n)
    MatMulRec(A[n:,:n],B[:n,:n],C[n:,:n], n)
    MatMulRec(A[n:,n:],B[n:,:n],C[n:,:n], n)
    MatMulRec(A[n:,:n],B[:n,n:],C[n:,n:], n)
    MatMulRec(A[n:,n:],B[n:,n:],C[n:,n:], n)



#MatMulRec(A,B,C,size)

print(A)
print(B)
print(ans)
print(C)