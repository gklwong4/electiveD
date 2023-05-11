A = [4,3,1,8,6]
i=1
j=2
while i < 5:
    if A[i] >= A[i-1]:
       i = j
       j += 1
    else:
        A[i],A[i-1] = A[i-1],A[i]
        i -= 1
        if i == 0:
            i = 1
    print(A)
