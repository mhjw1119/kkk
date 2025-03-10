import sys
sys.stdin = open('input.txt','r')

def search (y,x) :
    part_result = 0
    count = 0
    if arr[y][x] == 1 :
        part_result = M
    for k in range(1,N+1) :
        if -1 < y- k and y + k < N and -1 < x - k and x + k < N :
            for ny in range( y - k,y +k) :
                for nx in range(x - k, x + k) :
                    if arr[ny][nx] == 1:
                        part_result += M
                        count += 1
        if k * k + (k - 1) * (k - 1) < part_result :
            return count

        else:
            return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N) :
        for j in range(N) :
            result = max(search(i, j), result)
    print(result)