
def merge(A1,A2, A3):
    i = 0
    j = 0
    while i<len(A1) and j<len(A2):
        if A1[i]<=A2[j]:
            A3.append(A1[i])
            i+=1
        else:
            A3.append(A2[j])
            j+=1
    if i<len(A1):
        for ele in A1[i:]:
            A3.append(ele)
    elif j<len(A2):
        for ele in A2[j:]:
            A3.append(ele)
    
    return A3

def mergeSort(A,n):
    if n==1:
        return A
    
    else:
        A1 = mergeSort(A[0:n//2],n//2)
        A2 = mergeSort(A[n//2:], n//2 + n%2)
        A3 = []
        #print(A1,A2)
        return merge(A1,A2,A3)