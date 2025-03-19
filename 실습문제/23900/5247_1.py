import sys
sys.stdin = open( 'input.txt', 'r')

def check( num, cnt ) :
    global result
    if num == M :
        result = min(result, cnt)
        return
    if result <= cnt or num < 0:
        return

    if 0 > num :
        return

    for i in range(4) :
        if i == 0 :
            # check( num  - 10, cnt+1)
            check(num+1, cnt+1)
        if i == 1 :
            # check( num * 2 , cnt+1)

            check(num - 1, cnt+1)
        if i == 2 :
            check( num * 2 , cnt+1)
            # check(num - 1, cnt+1)

        if i == 3 :
            check( num  - 10, cnt+1)
            # check(num+1, cnt+1)



T = int(input())


for tc in range( 1, T + 1 ):
    N, M = map(int, input().split())
    result = 10000000000000000000000
    check(N, 0)

    print(f'#{tc} {result}')
