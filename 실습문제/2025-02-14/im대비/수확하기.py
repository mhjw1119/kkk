
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    p = [list(map(int,input())) for _ in range(N)]
    print(N,p)

    for i in range(N) :
        for low in range(N-(N//2)-i,i+N-(N//2)) :
            result += p[i][low]



    '''
     정가운데 인덱스를 찾은 다음 그 부분에서 부터 델타로 정리하면된다.
     정가운데는 바로 값을 넣을테니 상관없고, 상하좌우 그리고 대각선이 문제다.
     그래서 먼저 상하좌우를 정리한다.
     그리고 대각선이 존재하고 왼쪽 대각선의 왼쪽과 위에가
     
     아니다   정가운데 x좌표는 다 색칠이니까 정가운데 먼저하고 
     위로 올라갈 때 마다 양쪽으로 x의 값을 1씩 감소시킨다
     결국 가운데 위 아래 세개로 나누어서 처리한다.
     
    '''

    result = 0

    for i in range(N) :

        result += p[N//2][i]        #  가운데 값 완료
    result += p[0][N//2]
    result += p[N//2][0]

    # for high in range(N-(N//2)-1) :    # 윗값 아래로 내려올때 y값
    #     for low in range(1,N-(N//2)-1+(high*2)-1) :  #윗값에 증가 크기 설정
    #         if low == 1 :
    #             continue
    #         result += p[high][low]
    #
    # for high in range((N - (N // 2) - 1),1):  # 윗값 아래로 내려올때 y값
    #     for low in range(1, N - (N // 2) - 1 + (high * 2)-1):  # 윗값에 증가 크기 설정
    #         if low == 1:
    #             continue
    #         result += p[high][low]


    # for high in range(N-(N//2)) :
    #     if high == 0 :
    #         result += p[0][N-(N//2)]
    #         continue
    #     for low in range(N-(N//2)-high-1,N-(N//2)+high+1) :
    #         result += p[high][low]
    #
    # for high in range(N-(N//2),N) :
    #     if high == 4 :
    #         result += p[4][N-(N//2)]
    #         continue
    #     for low in range(1,N-high-2) :
    #         result += p[high][low]

    # for high in range(N-(N//2),1) :
    #     for low in range(N-2, 1, 2):  # 윗값에 증가 크기 설정
    #         for minus in range(N - (N // 2) - 1):
    #             next_idx = N - (N // 2) - 1 - minus  # 2 1 0
    #             for i in range(low):  # 증가 크기에 맞춘 반복문 1,3,5,7,,,
    #                 result += p[high][next_idx + i]


    print(result)