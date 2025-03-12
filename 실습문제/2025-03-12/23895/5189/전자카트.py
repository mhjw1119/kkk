# def search(visit,idx, kk,cnt ) :
#
#
#
#


T = int(input())


for tc in range ( 1, T +1 ):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = []
    check = [0] * N
    search_list = []
    search_result = []
    for i in range(2,N+1):
        path.append(i)

