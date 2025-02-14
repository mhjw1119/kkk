def seq_search(a,n,key) :
    for i in range(n) :
        if a[i] == key :

            return i
    return -1



arr = [4,9,11,23,2,19,7]

print(seq_search(arr, len(arr),8))

key = 11
ans = -1


