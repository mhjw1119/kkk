#  스타트에서 k만큼 더한다. 스타트 + k > 충전기 인지 확인한다.
# 그렇게 되면 이동 값을 충전기 값으로 바꾼다
# 반복한다.



# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k,n,m = map(int, input().split())
    # n = int(input())
    # m = int(input())
    road = list(input().split())

    start = 0
    count = 0
    for i in range(m) :
        if int(start + k) > int(road[i]) :
            for z in (i+1, m) :
                if int(start + k) <= int(road[z]) :
                    start = int(road[z])
                    count += 1
                    break
        print(f'#{test_case} {count}')
