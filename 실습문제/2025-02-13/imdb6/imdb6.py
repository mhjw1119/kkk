import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 일단 두 배열이 똑같은 위치에서 시작한다. 반복문으로 짧은 배열의 인덱스 길이에 맞춰서 같은
# 인덱스의 값을 곱하고 전부 더한다. 이후 짧은 반복문의 인덱스를 하나씩 증가시킨다. 이 때 범위는
# 짧은 범위를 이동하되, 인덱스 M값을 넘어가면 안된다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    # M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    max_result = 0
    for i in range(M-N+1) :
        if  i <= M-N :
            for search in range(3) :
                result += A[search] * B[i+search]
        max_result = max(result,max_result)
    print(max_result)