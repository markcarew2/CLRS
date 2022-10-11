def binSearchWrapper(A,x,a,b):
    from mergeSort import mergeSort
    A = mergeSort(A,len(A))
    return binarySearch(A,x,a,b)

def binarySearch(A,x,a,b):

    n = b-a
    midpoint = (b+a)//2

    if n==1 and A[a]!=x:
        return "Nil"
    
    else:
        if A[midpoint]>x:
            a = binarySearch(A, x, a, midpoint)
        elif A[midpoint] < x:
            a = binarySearch(A, x, midpoint,b)
        elif A[midpoint] == x:
            return midpoint

        return a

A = [1,3,5,8,6,9,11,14,17]


print(binSearchWrapper(A, 8, 0,len(A)))