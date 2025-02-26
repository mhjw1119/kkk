#
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    stack = []
    result = []
    top = -1
    count =0
    for i in range(1,N+1) :
        for x in range(i):
            if x != 0 and x != i-1 :
                result.append(stack[top]+stack[top-1])
                stack.append(stack[top]+stack[top-1])
                top -= 1
            else:
                stack.append(1)
                result.append(1)
        top = len(stack)-1
    index = 0
    print(f'#{test_case}')
    for i in range(1, N + 1):
        print(" ".join(map(str, result[index:index + i])))  # row 단위로 출력
        index += i

