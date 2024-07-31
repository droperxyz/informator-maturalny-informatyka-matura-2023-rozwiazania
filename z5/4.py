def W(j):
    while j > 1:
        if A[j] < A[j-1]:
            t = A[j]
            A[j] = A[j-1]
            A[j-1] = t
        j -= 1
    
A = [1,5,2,3,6,3]

W(5)

print(A)
    
