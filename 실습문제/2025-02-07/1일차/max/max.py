
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,(input().split()))
    ai = list(map(int, input().split()))
    max_list = [0] * (N-M+1)
    for i in range(N-M+1) :
        for x in range(i,i+M) :
            if i == (N-M+1) :
                break
            else :
                max_list[i] += ai[x]
    print(f'#{test_case} {max(max_list) - min(max_list)}')







    #----------------------------------------------------
    # three = 0
    # max_list = [0] *(N-(M-1))
    # for i in range(((M-1)//2),N-((M-1)//2)) :
    #
    #     for x in range(i-((M-1)//2),i+((M+1)//2)):
    #     #     three += ai[x]
    #     # max_list[i-((M-1)//2)] = three
    #         max_list[i - ((M - 1) // 2)] += ai[x]
    #     three = 0
    # print(max_list)
    # print(max(max_list),min(max_list))
    #
    # print(f'#{test_case} {max(max_list) - min(max_list)}')