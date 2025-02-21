import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    testca = int(input())
    arr = [list(input()) for _ in range(100)]


    def bfs(i, j):
        q = []
        check = [[0] * 100 for _ in range(100)]
        q.append([i, j])
        check[i][j] = 1
        flag = 0
        # print(len(q))

        while q:
            i, j = q.pop(0)
            if arr[i][j] == '3':
                return 1
            for dr in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + dr[0]
                nj = j + dr[-1]
                if -1 < ni < 100 and -1 < nj < 100 and arr[ni][nj] != '1' and check[ni][nj] != 1:
                    q.append([ni, nj])
                    check[ni][nj] = 1
        return 0


    i = 1
    j = 1
    result = bfs(i,j)

    print(f'#{testca} {result}')




