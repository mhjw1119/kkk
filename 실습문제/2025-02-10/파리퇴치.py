# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

'''
인덱스로 순회 하면서 해당 인덱스에서 파리채의 크기 만큼 x,y값을 이동시키면서 해당 인덱스에 값들을 다 더한다.

'''
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0
    for y in range(N):                          #순회 할 때 y 인덱스 값
        for x in range(N) :                     #순회 할 때 x 인덱스 값

            result = 0
            if x < N-M+1 and y < N-M+1:
                for yy in range(M) :
                    for xx in range(M):
                        print(fly[x+xx][y+yy])
                        result += fly[x+xx][y+yy]
                max_result = max(max_result, result)


    print(f'#{test_case} {max_result}')

    # ///////////////////////////////////////////////////////////////////////////////////
