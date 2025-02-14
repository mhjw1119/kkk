#  스타트에서 k만큼 더한다. 스타트 + k > 충전기 인지 확인한다.
# 그렇게 되면 이동 값을 충전기 값으로 바꾼다
# 반복한다.



import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ladder = [list(map(int, input().split()))for _ in range(100)]
    y = -1
    x = ladder[-1].index(2)
    count = 0
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    # print(ladder[-1].index(2))
    while y != -99 :
        for count in range(3):
            nx = x + dx[count]
            ny = y + dy[count]
            if nx < 0 or nx > 99 or ny < 0 or ny > 99:
                continue
            

        print(x)




    # print(ladder)

    # print(f'#{test_case} {max(result)}')
