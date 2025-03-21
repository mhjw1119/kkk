import sys
import heapq

sys.stdin = open('input.txt', 'r')


def dijkstra():
    backup = [(0, 0, 0)]
    while backup :
        weight, y, x = heapq.heappop(backup)
        if y == N-1 and x == N -1 :
            return weight

        weight += arr[y][x]
        if weight < check[y][x] :
            check[y][x] = weight
        else :
            continue

        for dy, dx in [0,1],[1,0],[0,-1],[-1,0]:
            ny = dy + y
            nx = dx + x
            if -1 < ny < N and -1 < nx < N :
                if nx == 0 and ny == 0 :
                    continue
                heapq.heappush( backup, (weight, ny, nx) )
T = int(input())

for tc in range( 1, T + 1 ) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    real = 1000000000000000000000000000000000000000000000000000000000
    check = [[1000000000000000000000000000000000000000000000000000000000] * (N) for _ in range(N)]
    print(f'#{tc} {dijkstra()}')
