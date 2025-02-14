def seq_search(a,n,key) :
    for i in range(n) :
        if a[i] == key :
            return i
        elif a[i] > key :
            return -1
    return -1       # 모든 원소가 key보다 작으면


arr = [4,9,11,23,2,19,7]
print(arr)
print((seq_search(arr, len(arr),11)))
print((seq_search(arr, len(arr),100)))