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
        su = fire.popleft()
        su[0] //= 2
        if su[0] == 0 :

            if count < M :
                fire.appendleft([arr[count],count +1 ])
                count += 1
                back = fire.pop()
                fire.appendleft(back)
            else:
                back = fire.pop()
                fire.appendleft(back)

        else:
            fire.appendleft(su)
            back = fire.pop()
            fire.appendleft(back)
    print(f'#{test_case} {fire[0][-1]}')
