def recur(cnt,search_list):     #cnt 재귀 호출마다 누적되어서 전달되어야 하는 값
    global search_result
    if cnt == len(path) :
        if len(search_list) == len(path):
        # for i in path :
        #     if i  == 0 :
            back = search_list[:]
            search_result.append(back)
        return
    for ne in range(len(path)):
        #이미 뽑았다면 뽑지 마라
        # if ne in path:
        #     continue
        if visit[ne] is True :
            continue
        visit[ne] = True
        search_list.append(path[ne])
        recur(cnt+1,search_list)
        search_list.pop()
        visit[ne] = False
def s ( ar ):
    real_result = []
    result = [1]
    result_sum = 1000000000
    back = 0
    for x in ar :
        for argu in x :
            result.append(argu)
        result.append(1)
        real_result.append(result)
        result=[1]
    for aa in real_result:
        for ggg in range(len(aa)-1):
            back += arr[aa[ggg]-1][aa[ggg+1]-1]
        result_sum = min(result_sum,back)
        back = 0
    return result_sum

T = int(input())


for tc in range ( 1, T +1 ):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = []
    result1 = 10000000000

    search_list1 = []
    search_result = []
    for i in range(2,N+1):
        path.append(i)
    visit = [False] * (len(path)+1)
    recur(0,search_list1)
    result1 = min(result1, s(search_result))

    print(f'#{tc} {result1}')

