'''
오버핸드 셔플 :   덱
int(0.37 * N)만큼 맨 뒤에서 카운트해서 앞으로 가져옴
퍼펙트 셔플 :    큐
int(0.5 * N)만큼 맨 뒤에서 떼어내서 배열에 담아두고
원래배열에 있는 넘들 큐에 하나 넣고 그 다음에 맨 뒤에서 떼어낸 배열 하나씩 넣는다.
'''
from collections import deque

def overhand ( N1 ) :
    over_b = int(0.37 * N1)
    if over_b  == 0 :
        return
    global arr
    over = deque()
    for o in range(N1):
        over.append(arr[o])

    for _ in range(over_b) :
        over.appendleft(over.pop())
    arr = over



def perf ( N2 ) :
    global arr
    perf_b = int(0.5 * N2)
    if perf_b == 0 :
        return
    perf_arr = []
    stack = []
    for p in range(N2-perf_b,N2 ) :
        perf_arr.append(arr[p])
    for _ in range(perf_b) :
        arr.pop()
    for pe in range(N2 - perf_b):
        stack.append(arr[pe])
        if pe < len(perf_arr):
            stack.append(perf_arr[pe])
    arr = stack



T = int(input())

for tc in range(1,T+1) :
    check = 1
    arr_N, N = map(int, input().split())
    arr = []
    for i in  range(arr_N) :
        arr.append(i+1)

    for _ in range(N) :
        overhand(arr_N)
        perf(arr_N)

    result = ''
    for qq in arr :
        result += str(qq)
    print(f'#{tc} {" ".join(result)}')