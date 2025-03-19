import sys
sys.stdin = open( 'input.txt', 'r')

def check( num, cnt ) :
    global result
    back = 0
    if num == M :
        if cnt < result :
            result = cnt
        return
    if result <= cnt or num < 0:
        back = -1
        return

    if 0 > num :
        back = -1
        return

    for i in range(4) :
        if num < M :

            if i == 0 :
                back = check( num * 2 , cnt+1)
                if back == -1 :
                    return
                # check(num - 1, cnt+1)
            if i == 1 :
                # check( num  - 10, cnt+1)
                check(num+1, cnt+1)
                if back == -1 :
                    return

        else:
            if i == 2 :
                check( num  - 10, cnt+1)
                if back == -1 :
                    return
                # check(num+1, cnt+1)

            if i == 3 :
                # check( num * 2 , cnt+1)

                check(num - 1, cnt+1)
                if back == -1 :
                    return





T = int(input())


for tc in range( 1, T + 1 ):
    N, M = map(int, input().split())
    result = 10000000000000000000000
    check(N, 0)

    print(f'#{tc} {result}')
