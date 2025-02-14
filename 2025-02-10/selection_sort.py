arr = [10, 25, 64, 22, 11]

def selection_sort(a,n) :
    for i in range(n-1) :
        min_idx = i
        for j in range(n) :
            if a[min_idx] > a[j] :
                min_idx = j
        a[i],a[min_idx] = a[min_idx], a[i]

selection_sort(arr,len(arr))
print(arr)