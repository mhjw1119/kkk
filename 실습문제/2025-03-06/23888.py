def two( N , count, back, log ) :
    if N == -1 :
        return

    if arr[N] == 1 :
        back += 2 ** log
    if count == 6 :
        result.append(back)
        log = -1
        count = -1
        back = 0
    two(N-1,count+1, back, log+1)


arr = list(map(int, input()))
n = len(arr)-1
result = []
two(n,0,0,0)
result = list(reversed(result))
print(result)