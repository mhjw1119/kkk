# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

'''
2의 인덱스 값을 알아내서 해당 좌표에서 출발한다.
해당 좌표에서부터 델타로 위 오른쪽 왼쪽을 탐색한다. 이때 좌우를 먼저 확인해서 좌우에 1이 있으면 그 방향으로 간다
근데 문제는 방향전환이 끝나도 해당 인덱스에서 방향전환을하는 무한 루프를 돌게 된다
그렇담 일단 무조건 왼쪽으로 간다. 방향전환이 되면 왼쪽이면 레프트 오른쪽이면 라이트를 넣는다. 이후 다시 방향 전환이
일어날 때 가지고 있는 방향과 다른 방향이 방향전환 버퍼에 들어가 있다면 방향전환이 아닌 상승한다.

'''

import sys
sys.stdin = open("input.txt", "r")

# T = int(input())

for test_case in range(1, 11):
    testcase = int(input())
    ladder = [list(map(int, input().split()))for _ in range(100)]
    y = 99
    x = ladder[-1].index(2)                         # [위][양옆]
    # print(ladder[-1].index(2))
    direction = 3
    dx = [-1,1,0]
    dy = [0,0,-1]
    count = 4
    # print(ladder[-1][57])
    while y != 0 :


        for i in range(3) :
            nx = dx[i] + x
            ny = dy[i] + y

            # 왼쪽에 1이 있으면 1쪽으로 한칸 간다
            if  nx >= 0 and nx < 100 :  #만약 인덱스 a값이 벗어나면 해당 포문을 돌리지 않는다.
                if ladder[ny][nx] == 1 :            # 만약 좌우 위에 1이 있다면
                    if i == 0 :             #만약 왼쪽으로 간다면 그리고 첫 방향전환이라면
                        if direction == 3 :
                            x = nx
                            y = ny
                            direction = 0  # 0을 삽입
                            break

                        if direction == 1:  # 왔던 방향으로 다시 가려고 하면 컨티뉴 해라
                            direction = 3
                            continue


                        direction = 0       # 0을 삽입
                    if i == 1 :
                        if direction == 3:
                            x = nx
                            y = ny
                            direction = 1  # 0을 삽입
                            break

                        if direction == 0:  # 왔던 방향으로 다시 가려고 하면 컨티뉴 해라
                            direction = 3
                            continue

                        direction = 1       # 오른쪽이면 1을 삽입

                    x = nx
                    y = ny
                    break

    print(f'{testcase} {x}')