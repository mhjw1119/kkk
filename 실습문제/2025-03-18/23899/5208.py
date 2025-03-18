'''
재귀로 해당 정류장에 있는 충전지 수 만큼 전진하여 도착지까지 가는지 확인
이 때 가지치기로 만약 횟수가 최소 수 보다 커지면 중단 ㄱㄱ
'''

def check ( start, cnt ):
    global result
    if cnt > result :
        return
    if start < N - 1 :
        if cnt + min(bus_stop[start:]) > result :
            return

    if start >= N-1 :
        result = min(result,cnt)
        return

    for i in range(1, bus_stop[start]+1 ):
        if start + i < N :
            check( start + i ,cnt + 1)




T = int(input())

for tc in range( 1,  T + 1 ):
    ipt = list(map(int,input().split()))
    N = ipt[0]
    bus_stop = ipt[1:]
    result = 10000
    check(0,0)
    print(f'#{tc} {result - 1}')
