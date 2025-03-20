import sys
from collections import deque

sys.stdin = open( 'input.txt', 'r')

def check(  N, M ) :
    check_result = []
    visit = set([N])
    back = deque([(N,0)])
    while back :
        num, cnt = back.popleft()
        if num > 1000000 :
            return
        if num == M and num <= 1000000:
            return
        for i in [num*2,num - 10, num + 1,num - 1] :
            if 1<= i <= 1000000 and i not in visit :

                if i == M :
                    return cnt + 1

                back.append((i, cnt + 1))
                visit.add(i)
                # back.append((i, cnt + 1))
                # visit.add(i)

    # cnt += 1
    # check(back)

T = int(input())


for tc in range( 1, T + 1 ):
    N, M = map(int, input().split())
    result = check(N, M)
    print(f'#{tc} {result}')
