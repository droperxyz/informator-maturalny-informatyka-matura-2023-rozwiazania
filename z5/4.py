def W(j):
    while j > 1:
        if A[j] < A[j-1]:
            t = A[j]
            A[j] = A[j-1]
            A[j-1] = t
        j -= 1
  
