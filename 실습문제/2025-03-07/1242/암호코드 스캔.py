import sys
sys.stdin = open('input.txt', 'r')
check_hex = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
check_hex = '123456789ABCDEF'

def hex_to_bin( hx ) :
    cnt = 0
    hex_to_bin_result = ''
    chart = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    for k in hx:
        hex_to_bin_result = hex_to_bin_result + chart[k]

    return hex_to_bin_result

def two( arr1 ) :
    cnt = 0
    arr1_cnt_result = []
    result = []
    arr1_str = ''
    arr1_cnt = 0
    arr1_r = 0
    code = ['3211','2221', '2122','1411','1132','1231','1114','1312','1213','3112']
    for _ in range(8) :
        for f in range(4) :
            arr1_cnt = 0
            while 1:

                if sum(arr1_cnt_result) + arr1_cnt >= 7 :
                    break
                arr1_cnt += 1
                if arr1[arr1_r] != arr1[arr1_r + 1] :
                    break

                arr1_r += 1
            arr1_cnt_result.append(int(arr1_cnt / low_cnt))
        for p in arr1_cnt_result :
            arr1_str = arr1_str + str(p)
        if arr1_str not in code :
            return
        for ch in range(8) :
            result.append(code.index(arr1_str))
    return result




    for k in range(8):
        if arr1[ k*7*cnt:(k*7)+7 ] not in code :
            return 0
        result.append(code.index(arr1[ k*7:(k*7)+7 ]))

    return result

def check ( ar ) :
    if not ar :
        return 0
    a = 0
    b = 0
    for y in range(0,len(ar),2) :
        if y == 7 :
            continue
        a += ar[y]
    for y in range(1,len(ar),2) :
        if y == 7 :
            continue
        b += ar[y]

    if ((a * 3) + b + ar[7]) % 10 == 0 :
        return a + b + ar[7]
    else:
        return 0


T = int(input())

for testcase in range(1, T+ 1):
    N, M = map(int,input().split())
    arr = [str(input()) for _ in range(N)]
    backup_hex_arr = []
    bin_arr = []
    for i in range(N) :
        for j in range(len(check_hex)):
            if check_hex[j] in arr[i] and arr[i] not in backup_hex_arr:
                backup_hex_arr.append(arr[i])                           #16진수 배열 후보군 저장 완료
    for i in backup_hex_arr :
        bin_arr.append(hex_to_bin(i))                                   # 후보군들 전부 16진수 2진수로 변환 완료

#----------------------------------------------------------------------------
    line = 0
    end = 0
    sum_bin = 0
    low_cnt = 1
    for i in range(len(bin_arr)) :
        start = bin_arr[i].index('1')

        for i2 in range(M-1,0,-1) :
            if bin_arr[i][i2] == '1':
                end = i2
                break                                         # 시작점 마지막 찾기
        low_check = end - start
        while low_check > 0 :
            low_check //= 2
            low_cnt += 1

        low = (55 * low_cnt)- (end - start)

        if low != 0 :
            for i3 in range(7*low_cnt) :
                if 0 <= start -i3:
                    backup = bin_arr[i][start-i3:start + 55*low_cnt]
                    real_result = two(backup)
                    if real_result != 0 :
                        real_result  = check(real_result)
                        sum_bin += real_result
                    if real_result != 0:
                        break

        else:
            backup = bin_arr[i][start:end+2]
            real_result = check(two(backup))
            sum_bin += real_result

    print(f'#{testcase} {sum_bin}')








