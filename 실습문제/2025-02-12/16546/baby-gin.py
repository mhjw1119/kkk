
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    card = list(map(int, input().strip()))
    count = 0
    backup = [0] * 10
    for i in range(6) :
        backup[card[i]] += 1
    i = 0
    while i < 9 :
        if backup[i] > 0 :
            if i < 8:
                if backup[i] >0 and backup[i+1] > 0 and backup[i+2] > 0 :
                    count += 1


                    for x in range(3) :
                        backup[x+i] -= 1
                    i = 0
                if backup[i] >= 3 :
                    backup[i] - 3
                    count += 1
                    i = 0

        i += 1


        if count == 2 :
            result = 'true'
            break
        else:
            result = 'false'




    # print(card)
    print(f"#{test_case} {result}")

    # 연속된 숫자 먼저 검증 이후 트리플




    # ///////////////////////////////////////////////////////////////////////////////////
