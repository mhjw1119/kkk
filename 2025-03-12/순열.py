
path = []
visit = [False] * 7
def recur(cnt):     #cnt 재귀 호출마다 누적되어서 전달되어야 하는 값
    if cnt == 3 :
        # for i in path :
        #     if i  == 0 :
        print(path)
        return
    for ne in range(1,7):
        #이미 뽑았다면 뽑지 마라
        # if ne in path:
        #     continue
        if visit[ne] is True :
            continue
        visit[ne] = True
        path.append(ne)
        recur(cnt+1)
        path.pop()
        visit[ne] = False

#제일 처음 호출 할 때 시점
recur(0)

