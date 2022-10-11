import numpy as np

def countSort(A, n, b, place):
    C = [0] * (b+1)
    B = [0] * n
    
    for j in A:
        index = j // place
        print(index)
        C[index % b]+=1

    for i in range(1,b):
        C[i] += C[i-1]
        
    for i in range(n,0,-1): 
        B[C[A[i-1]//place%b]-1] = A[i-1]
        C[A[i-1]//place%b] = C[A[i-1]//place%b] - 1
        print(B)
    
    return B

def radixSort(A, n, d,b):
    D = A
    for i in range(d):
        place = 10**i
        D = countSort(D, n, b, place)
    return D



k = 11
n = 10
d = 2
b = 10
A = np.random.randint(k, size=n)

print(A)

print(radixSort(A, n,d,b))
