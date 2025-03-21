import sys
sys.stdin = open('input.txt', 'r')
def dfs (y,x, result) :
    global real
    if y == N-1 and x == N-1 :
        real = min(result, real)
        return
    if result > real :
        mine[y][x] = 1
        return

    result += arr[y][x]
    check[y][x] = 1

    if result > real :
        return
    check_min = [10000,0,0]

    for dy, dx in [0,1],[1,0],[0,-1],[-1,0] :
        ny = dy + y
        nx = dx + x
        if -1 < ny < N and -1 < nx < N and check[ny][nx] != 1 and mine[ny][nx] != 1:
            dfs(ny, nx, result)
            check[ny][nx] = 0


T = int(input())

for tc in range( 1, T + 1 ) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    real = 1000000000000000000000000000000000000000000000000000000000
    check = [[0] * (N) for _ in range(N)]
    check[0][0] = 1
    mine = [[0] * (N) for _ in range(N)]
    dfs(0,0, 0)
    print(f'#{tc} {real}')
