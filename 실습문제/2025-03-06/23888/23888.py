import  sys
sys.stdin = open('input.txt', 'r')

def two( N , count, back, log ) :
    if N == len(arr1) :
        return

    if arr1[N] == '1' :
        back += 2 ** log
    if count == 6 :
        result.append(str(back))
        log = 7
        count = -1
        back = 0
    two(N+1,count+1, back, log-1)


T = int(input())

for testcase in range(1,T+1) :
    N1 = int(input())
    arr1 = ''
    for i in range(N1) :
        ai = str(input())
        arr1 = arr1 + ai
    # for i in range(N1) :
    n = len(arr1)-1
    result = []
    two(0,0,0,0)
    # result = list(reversed(result))
    print(f'#{testcase} {" ".join(result)}')