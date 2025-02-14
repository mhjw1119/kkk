
'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
sys.stdin = open("input.txt", "r")
length = 100
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(length)]

    # 대각선의 합
    sum_cross = 0
    for i in range(length) :
        sum_cross += arr[i][i]

    # 행의 합    세로는 가만히 있고 가로 값만 증가
    sum_hang = [0]*100
    for i in range(length) :
        for x in range(length) :
            sum_hang[i] += arr[i][x]
    result_hang = max(sum_hang)



    # 열의 합   이번에는 가로는 가만히 있고 세로값만 증가
    sum_se = [0]*100

    for i in range(length) :
        for x in range(length) :
            sum_se[i] += arr[x][i]
    result_se = max(sum_se)

    result_list = []
    result_list.append(result_se)
    result_list.append(sum_cross)
    result_list.append(result_hang)
    print(f'#{test_case} {max(result_list)}')








