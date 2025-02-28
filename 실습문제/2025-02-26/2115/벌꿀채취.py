from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N) :
        for j in range(N-M+1):
            f_sum = []
            f_sum.append(arr[i][j])
            f_sum.append(arr[i][j+1])
            for sel in range(M) :
                f_sum = [combinations(f_sum,sel)]
                for f in range(len(f_sum)):
                    if sum(f_sum[i]) <= 10 :
                        for s in range(f_sum)







