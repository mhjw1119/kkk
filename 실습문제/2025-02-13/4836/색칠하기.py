
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    chart = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(N) :
        r1, c1, r2, c2, color = map(int,input().split())
        # 2   2    4  4
        # 22  24   42 44
        for i in range(r2-r1+1) :
            for j in range(c2 - c1+1) :
                chart[r1+i][c1+j] += color
    for i in range(10) :
        for j in range(10) :
            if chart[i][j] != 1 and chart[i][j] % 2 == 1 :
                result += 1

    print(f"#{test_case} {result}")