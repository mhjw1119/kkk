import sys
sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    count = N
    fire = []
    for i in range(N) :
        fire.append([arr[i],i+1])

    while len(fire) != 1 :
        for i in range(N) :
            if i >= len(fire):
                break
            if fire[i][0] == 0 :
                if count < M:
                    fire[i] = [arr[count], count+1 ]
                    count += 1
                else :

                    fire.pop(i)
            else:
                fire[i][0] //= 2
    print(fire[-1])
