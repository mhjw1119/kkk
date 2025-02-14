
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,K = map(int,input().split())
    box = [0] * (N+1)
    box = [0] * 12

    for i in range(12) :
        box[i] = i+1

    result = 0
    # for i in range(1,13) :
    #     for x in range(N) :
    #         box[x] = i+x
    #     if sum(box) == K :
    #         result += 1
    # print(f"#{test_case} {result}")
    for i in range(1<<12) :
        backup = []
        for j in range(12):
            if i&(1<<j) :
                backup.append(box[j])
        if len(backup) == N and sum(backup) == K :
            result += 1



    print(f"#{test_case} {result}")