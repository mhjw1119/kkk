
def check(line, depth, data):
    global result
    global check_x
    global max_sum
    if data >= result:
        return
    if depth == N :
        if result > data:
            result = data
        return
    for i in range(N):
        if check_x[i]:
            continue
        check_x[i] = 1
        check(line+1, depth+1, data + arr[depth][i])
        check_x[i] = 0
T = int(input())
for tc in range( 1, T + 1 ):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000
    backup=[]
    check_x = [0] * (N+1)
    check_x_first = []
    check(0,0, 0)
    print(f'#{tc} {result}')