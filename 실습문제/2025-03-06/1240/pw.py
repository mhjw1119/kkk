import sys
sys.stdin = open('input.txt', 'r')

def two( arr1 ) :
    cnt = 0
    result = []
    code = ['0001101','0011001', '0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    for k in range(8):
        if arr1[ k*7:(k*7)+7 ] not in code :
            return 0
        result.append(code.index(arr1[ k*7:(k*7)+7 ]))

    return result

def check ( ar ) :
    if not ar :
        return 0
    a = 0
    b = 0
    for y in range(0,len(ar),2) :
        a += ar[y]
    for y in range(1,len(ar),2) :
        b += ar[y]
    if ((a * 3) + b) % 10 == 0 :
        return a + b
    else:
        return 0

T = int(input())

for testcase in range(1, T+ 1):
    n, M = map(int,input().split())
    arr = [str(input()) for _ in range(n)]
    line = 0
    end = 0
    real_result = [[] for _ in range(7)]
    re = 0
    for i in range(n) :
        if '1' in arr[i] :
            line = i
            break
    start = arr[line].index('1')

    for i in range(M-1,0,-1) :
        if arr[line][i] == '1':
            end = i
            break
    low = 55 - (end - start)

    backup = []
    if low != 0 :
        for i in range(low+1) :
            backup = str(arr[line][start-i:-1])
            real_result = two(backup)
            if real_result != 0 :
                real_result  = check(real_result)
            if real_result != 0:
                break

    else:
        backup = str(arr[line][start:end+2])
        real_result = check(two(backup))

    print(f'#{testcase} {real_result}')





