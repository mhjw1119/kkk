import sys
sys.stdin = open('input.txt','r')

chart = {'0': '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001','A' : '1010','B' : '1011','C' : '1100', 'D' : '1101', 'E' : '1110','F' : '1111'}
T = int(input())

def to_hex ( arr ) :
    for i in range(int(N)) :
        if arr[i] in chart :
            result.append(chart[arr[i]])


for tc in range(1,T+1) :
    N, arr1 = list(map(str, input().split()))
    result = []
    to_hex(arr1)

    print(f'#{tc} {"".join(result)}')