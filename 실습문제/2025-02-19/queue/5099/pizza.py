import sys
sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    fire = deque()


    for i in range(N) :
        fire.append([arr[i],i+1])

    count = N

    while len(fire) != 1 :
        su = fire.popleft()                 # 핏짜 꺼내서 구워졌는지 확인
        su[0] //= 2
        if su[0] == 0 :                     #구워 졌다면

            if count < M :                                  # 그리고 남은 핏짜가 있다면 남은 핏짜 넣어라
                fire.append([arr[count],count +1 ])
                count += 1

        else:
            fire.append(su)                             #핏짜가 덜 구워졌다면 그 핏짜 다시 내려놔라

    print(f'#{test_case} {fire[0][-1]}')
