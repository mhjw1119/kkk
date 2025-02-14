

import sys
sys.stdin = open("input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    case = list(input()for _ in range(8))
    # def check (num, setting) :
    #     count = 0
    #     for i in range(num//2) :
    #         if setting[i] == setting[num] :
    #             count += 1
    #     if count == num//2 :
    #         return True
    # high_count = 0
    # low_count = 0
    result = 0
    for i in range(8) :

        for j in range(8) :
            high_count = 0
            low_count = 0
            for k in range( N // 2):
                # if j < 7-(N//2 ):
                if j <= 8 - N :
                    if case[j+k][i] == case[j+N-1-k][i]:
                        high_count += 1
                    else :
                        break

            if high_count == N//2 :
                result += 1

            for k in range(N // 2):
                if i <= 8 - N :
                    if case[j][i + k] == case[j][i + N-1 - k]:
                        low_count += 1
                    else:
                        break

            if low_count == N//2:
                result += 1
    print(f'#{test_case} {result}')    # ///////////////////////////////////////////////////////////////////////////////////
