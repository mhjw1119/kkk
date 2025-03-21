
import sys
sys.stdin = open('input.txt', 'r')

import heapq

def check ( y, x ) :
    heap = []
    while heap :
        y, x = heapq.heappop(heap)
        for dy, dx in [0,1],[1,0],[0,-1],[-1,0] :
            ny = dy + y
            nx = dx + x
            if -1 < ny < N and -1 < nx < N and visit[ny][nx] != 1 :
                heapq.heappush(heap,(arr[ny][nx], y, x))
                visit[ny][nx] = 1



T = int(input())

for tc in range( 1, T + 1 ) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    check(0,0)

    # print(f'#{tc} {real}')
