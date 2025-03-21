#  스타트에서 k만큼 더한다. 스타트 + k > 충전기 인지 확인한다.
# 그렇게 되면 이동 값을 충전기 값으로 바꾼다
# 반복한다.



import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    bum = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    result = -1
    index = 0

    for i in range(N) :
        for j in range(M) :

            result = bum[i][j]
            for dir in range(4) :
                nx = i + dx[dir]
                ny = j + dy[dir]
                if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                    continue
                result += bum[nx][ny]

                result = max(result, bum[nx][ny])

            index += 1

    print(f'#{test_case} {result}')
