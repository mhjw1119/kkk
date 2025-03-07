import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def to_bin(target,cnt) :
    global check
    if target == 0 :
        return
    if cnt >= 12 :
        check = -1
        return

    target *= 2
    if target >= 1 :
        cnt += 1
        result.append('1')
        target -= 1
        to_bin(target,cnt)

    else:
        cnt += 1
        result.append('0')
        to_bin(target,cnt)




for tc in range( 1, T+1) :
    arr = float(input())
    result = []
    check = 0
    to_bin(arr,0)
    if check == -1 :
        result = 'overflow'
    print(f'#{tc} {"".join(result)}')
