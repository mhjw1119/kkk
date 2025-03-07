import  sys
sys.stdin = open()

T = int(input())


def solution() :
    target  = M
    for i in range(N) :
        if target & 0x1 == 0 :

            return False
        target = target >> 1
    return True


def solution2():
    mask = (1 << N) -1
    result = (M & mask) == mask
    return result


for tc in range(1,T+1) :


    N, M = map ( int , input().split())

    result = solution()