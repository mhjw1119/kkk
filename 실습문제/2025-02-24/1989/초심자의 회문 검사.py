import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = str(input())
    result = 1
    half = len(string)//2
    for i in range(half) :
        if string[i] == string[len(string)-i-1] :
            pass
        else:
            result = 0
            break
    print(f'#{test_case} {result}')
