from numpy.random import rand
import numpy as np

#INSERTION-SORT(A,n)
def insertionSort(A,n):
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

    return A

#Exercise 2.1-3
def insertionSortDecrease(A,n):
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]<key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

    return A

A = np.around((rand(100) * 1000))
n = len(A)
print(insertionSort(A,n))

print(insertionSortDecrease(A,n))