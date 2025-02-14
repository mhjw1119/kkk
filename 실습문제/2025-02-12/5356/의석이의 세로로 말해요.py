

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    useok = list(input() for _ in range (5))
    result = []
    length = [0] * (len(useok))

    for i in range(5) :
        length[i] = len(useok[i])
    for j in range(len(useok[i])):
        for  i in range (5) :
            if length[i] <= j :
                continue
            else:
                result.append(useok[i][j])



    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
