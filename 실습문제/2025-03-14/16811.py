'''
N개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다.
같은 크기의 당근은 같은 상자에 들어있어야 한다.
비어 있는 상자가 있으면 안 된다.
한 상자에 N/2개(N이 홀수면 소수점 버림)를 초과하는 당근이 있어서도 안 된다.
앞의 조건을 만족하면서도, 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다.
부분 집합 구하기. 근데 부분 집합 구한면 원 배열에서 집합 구한 거에서 삭제 시켜줘야한다.
'''

import sys
sys.stdin = open('input.txt','r')

def part ( ar, start):
    back = []
    if start == len(arr) :
        if N//2 >= len(ar) > 0 :
            result_arr.append(ar[:])
        return
    ar.append(arr[start])
    part(ar, start + 1)
    ar.pop()


    part(ar, start + 1)



def check (start, check_result) :
    if not check_result :
        check_result.append(result_arr[start])
    # if start == len(result_arr):
    #     return
    if 3 == len(check_result) :
        for i in check_result:
            result.append(i)
        return

    # check_result.append(result_arr[start])
    for i in range(len(result_arr)) :
        # check(start + 1, check_result)

        if i == start :
            continue
        if max(check_result[-1]) < max(result_arr[i]) and check_result[-1][-1] != result_arr[i][0]:
            check_result.append(result_arr[i])
            check(start+1,check_result)
        # check(start+1,check_result)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    real_result = 0
    result_arr = []
    part_ar = []
    result = []
    check_arr = []
    part(part_ar,0)
    check(0,check_arr)
    # print(result_arr)
    if not result :
        real_result = -1
    else:
        real_result = max( abs(result[0] - result[1]), abs(result[2] - result[1]), abs(result[0] - result[2]))

    print(real_result)

