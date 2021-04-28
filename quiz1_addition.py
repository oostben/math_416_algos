A = [9,9,9]
B = [9,9,9]
C = []


#ALGO
temp1 = 0
for i in range (len(A)-1,-1,-1):
    temp1 = A[i] + B[i] + temp1
    temp2 = temp1%10
    temp1 = temp1 // 10
    C.insert(0,temp2)
C.insert(0,temp2)


print(C)