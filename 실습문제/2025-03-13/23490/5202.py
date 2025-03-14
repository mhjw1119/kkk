import sys
sys.stdin = open('input.txt','r')

def check (s,e,cnt) :
    global result
    for ii in range(N) :
        if e <= start[ii] :
            check(start[ii],end[ii],cnt+1)

    result = max(cnt,result)




T = int(input())


for tc in range(1,T+1):
    hour = [0] * 24
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    start = []
    end = []
    result = 0
    for search in time :
        start.append(search[0])
        end.append(search[1])
    for i in range(N) :
        check(start[i],end[i],1)

    print(f'#{tc} {result}')
