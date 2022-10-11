import random

def swapElements(A, s, d):
    A[s], A[d] = A[d], A[s]
    
def randomPartition(A):
    s = random.randint(0,len(A)-1)
    swapElements(A, s, -1)
    print(A[-1])
    x = A[-1]
    i = -1
    for j in range(len(A)-1):
        if A[j] <= x:
            i+=1
            swapElements(A, i, j)

    swapElements(A, i+1, -1)
    q = i+1
    return q


def quickSort(A):
    if len(A) > 1:
        q= randomPartition(A)
        #print(less,q,more)
        return quickSort(A[:q]) + [A[q]] + quickSort(A[q+1:])

    else:
        return A

A = [1,4,2,5,7,9,10,3,17]
A = quickSort(A)
print(A)
