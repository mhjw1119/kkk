def s (n):
    for i in range(1,n) :
        if i * 2 < n :
            if arr[i] < arr[i*2] :
                arr[i],arr[i*2] = arr[i*2], arr[i]
        if (i * 2) + 1 < n:
            if arr[i] > arr[(i*2)+1] :
                arr[i], arr[(i*2)+1] = arr[(i*2)+1], arr[i]
    s(n+1)


T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    arr = [0]
    for j in range(1,N+1) :
        arr.append(j)
        s(j)
    print(arr[N//2])
