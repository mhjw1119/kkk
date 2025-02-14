# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.


#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int,input().split()))

    for i in range(N) :





    #---------------------------------------

    # my_max = ai[0]
    # my_min = ai[0]
    #
    # for i in range(N) :
    #     if my_min > ai[i] :
    #         my_min = ai[i]
    #     elif my_max < ai[i] :
    #         my_max = ai[i]
    # print(f'#{test_case} {my_max-my_min}')