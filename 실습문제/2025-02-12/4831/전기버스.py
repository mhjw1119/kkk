
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
        차에다가 충전기를 더한다.   차 값보다 충정
    '''

    K, N, M = map(int, input().split())
    charger = list(map(int,(input().split())))
    car = 0
    notgood = 8

    # road = [0] * N
    result = 0
    # for i in range (M) :
    #     road[charger[i]] = 1
    status = 0
    for i in range(N) :
        if notgood == 0 :
            break
        car += K

        if car >= N :
            break

        for x in range(M-1,-1,-1) :

            if car >= charger[x] and car-K < charger[x] :
                car = charger[x]
                result += 1
                break
            else :
                # status = 1
                if x == 0 :
                    notgood = 0
                    result = 0
                    break
                continue

    print(f"#{test_case} {result}")






    # ///////////////////////////////////////////////////////////////////////////////////
