'''
기준값을 입력 받아서 오른쪽 값들중에서 가장 큰 값을 기준값이랑 바꾼다
왼쪽이 다 같거나 크다면 다음 기준값으로 넘긴다.
기준값이 제일 큰 값과 같다면 다음 기준 값으로 넘긴다.
'''

def check (idx) :
    back = 0
    backup = []
    if idx == len(arr) -1 :
        arr[idx],arr[idx-1] = arr[idx-1], arr[idx]
        return

    if idx != 0 :
        if arr[idx] == arr_max or max(arr[:idx])<= arr[idx] :
            check(idx + 1)
        else:
            if idx < len(arr) :
                back = arr[idx]
                for i in range(idx+1,len(arr)):
                    if back < arr[i] :
                        back = arr[i]
                        backup = i
                arr[idx],arr[backup] = arr[backup],arr[idx]
                return
            else:
                check(0)
    else:
        if arr[idx] == arr_max :
            check(idx + 1)
        else:
            if idx < len(arr):
                back = arr[idx]
                for i in range(idx + 1, len(arr)):
                    if back < arr[i]:
                        back = arr[i]
                        backup = i
                arr[idx], arr[backup] = arr[backup], arr[idx]
                return
            else:
                check(0)




T = int(input())

for tc in range(1,T+1):

    real,N =  map(str,input().split())
    arr = []
    N = int(N)
    for i in real:
        arr.append(int(i))

    arr_max = max(arr)
    cnt = N
    for j in range(N) :
        check(0)

    print(arr)

