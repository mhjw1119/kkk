'''
종료 조건 : [N-1,N-1]일때
무조건 오른쪽으로 간다 벽에 막히면 아래로 간다
'''

def dfs (start) :
    global result
    global min_result
    y, x = start
    result += arr[y][x]

    if y == N-1 and x == N-1 :
        min_result = min(min_result, result)

        return

    if x + 1 <= N-1 :
        x += 1
        dfs([y,x])
        result -= arr[y][x]
        x -= 1
    if y+1 <= N -1 :
        y += 1
        dfs([y,x])
        result -= arr[y][x]
        y -= 1






T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    min_result = 10000000000000
    first = [0,0]
    dfs(first)

    print(f'#{tc} {min_result}')