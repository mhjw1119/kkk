
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    testcase = int(input())
    check = list(input())
    arr = list(input())
    count = 0
    result = 0
    for i in range(len(arr)) :
        if arr[i] == check[0] :
            for j in range(len(check)) :
                if arr[i+j] == check[j] :
                    count += 1
                    pass
                else:
                    break
                if count == len(check) :
                    result += 1
    print(f'#{testcase} {result}')
