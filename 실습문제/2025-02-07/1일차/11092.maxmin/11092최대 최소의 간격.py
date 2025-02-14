
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int,input().split()))

    x = max(ai)
    z = 0
    z = ai.index(min(ai))
    for i in range(N-1,0,-1):
        if ai[i] >= x :
            x = i
            break
    result = x - z
    if result < 0 :
        result = result * -1
    print(f'#{test_case} {result}')



    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
