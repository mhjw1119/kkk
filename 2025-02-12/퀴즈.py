A = 'xypv'
B = 'eoggxypvsy'
result = []

for i in range(0,len(B)-(len(B)-len(A)),2) :
    result.append(A[i])
    result.append(B[i])
    # result[i] = A[i]
    # result[i+1] = B[i]
result.append(B[len(B)-len(B)-len(A):len(B)+1])


print(''.join(result))