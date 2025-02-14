'''
각 단어에 맞는 진짜
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    org = (input().split())
    backup = [0] * N

    number = {"ZRO": 0}
    number["ONE"] = 1
    number["TWO"] = 2
    number["THR"] = 3
    number["FOR"] = 4
    number["FIV"] = 5
    number["SIX"] = 6
    number["SVN"] = 7
    number["EGT"] = 8
    number["NIN"] = 9


    for i in range(N) :
        backup[i] = number[org[i]]
    backup.sort()

    print(backup)

    # for i in range(N) :
    #     result[i] = number[backup[i]]






    print(org)
    print(number)

    # ///////////////////////////////////////////////////////////////////////////////////
