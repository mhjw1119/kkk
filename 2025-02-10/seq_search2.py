arr = [[1,2,3],[4,5,6],[7,8,9,]]

N = 3
key = 5
ans = 0         # key가 있으면 1, 없으면 0

def seq_search(arr,N,key) :
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                return 1
    return 0


for i in range(N) :
    for j in range(N) :
        if arr[i][j] == key :
            ans = 1
            break  # for j

