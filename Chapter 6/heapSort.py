
def swapEle(A, i, j):
    A[i],A[j] = A[j],A[i]

def MaxHeapify(A,i):
    l = 2*i +1
    r = 2*i + 2
    if l<A.heapSize and A.heap[i]<A.heap[l]:
        largest = l
    else:
        largest = i
    if r<A.heapSize and A.heap[largest]<A.heap[r]:
        largest = r
    if largest!=i:
        swapEle(A.heap, i, largest)
        MaxHeapify(A, largest)
    return A


class MaxHeap():
    def __init__(self, A):
        self.heapSize = len(A)
        self.heap = A

    def buildMaxHeap(self):    
        for r in range(int(self.heapSize/2),-1,-1):
            self = MaxHeapify(self,r)
        return self

        
A = [10,24,13,40,16,12,1,7,9,2]

def HeapSort(A, n):
    A = MaxHeap(A).buildMaxHeap()
    for i in range(n-1, 0,-1):
        swapEle(A.heap,0,i)
        A.heapSize = A.heapSize-1
        A = MaxHeapify(A,0)
    return A.heap



A = HeapSort(A, len(A))
print(A)