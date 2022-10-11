def binaryAddition(A,B,n):
    C = []
    remainder = 0
    for i in range(n):
        C.append((A[i] + B[i] + remainder) % 2)
        remainder = A[i] + B[i] // 2
    C.append(remainder)
    return C

def checkResult(C):
    sum = 0
    for i,ele in enumerate(C):
        sum = (ele * (2**i)) + sum
        
    return sum

A = [1,1,0,0]
B = [1,1,0,1]

C = binaryAddition(A,B,4)
print(C)
print(checkResult(C))
