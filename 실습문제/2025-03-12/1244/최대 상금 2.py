'''
기준값을 입력 받아서 오른쪽 값들중에서 가장 큰 값을 기준값이랑 바꾼다
왼쪽이 다 같거나 크다면 다음 기준값으로 넘긴다.
기준값이 제일 큰 값과 같다면 다음 기준 값으로 넘긴다.
'''

def check (cnt, start) :
    global result
    global result_arr
    backup = ''

    if cnt == N :
        for i in arr :
            backup += str(i)
        result_arr.append(int(backup))
        return

    if start >= len(arr) :
        return

    for i in range(len(arr)):
        arr[i], arr [start] = arr[start], arr[i]
        check(cnt + 1,start+1)
        arr[i], arr[start] = arr[start], arr[i]





T = int(input())

for tc in range(1,T+1):

    real,N =  map(str,input().split())
    arr = []
    result_arr = []
    N = int(N)
    visit = [0] * (len(arr) + 1)
    result = 0
    for q in real:
        arr.append(int(q))
    check(0,0)
    print(max(result_arr))
