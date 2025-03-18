import sys
sys.stdin = open('input.txt', 'r')
def check(y, x, check_list) :

    global result
    if len(check_list) == N :
        result1 = float(check_list[0]) * 0.01
        for i in range(1,N):
            result1 *= float(check_list[i]) * 0.01

        result = max(result,result1*100)
        return
    for i in range(x+1,N) :
        if i != x :
            check_list.append(arr[y][i])
            check(y+1,x, check_list)
            check_list.pop()
    # check_list.append(arr[y][x])
    # check(y+1, x, check_list)
    # check_list.pop()
    # check( y, x + 1, check_list )


T = int(input())

for tc in range( 1, T + 1 ):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    backup=[]
    check(0,-1,backup)
    print(f'#{tc} {result:.6f}')
