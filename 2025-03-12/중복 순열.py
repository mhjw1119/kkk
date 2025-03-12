
path = []
def recur(cnt):     #cnt 재귀 호출마다 누적되어서 전달되어야 하는 값
    if cnt == 3 :
        # for i in path :
        #     if i  == 0 :
        print(path)
        return
    for ne in range(1,7):
        path.append(ne)
        recur(cnt+1)
        path.pop()




    # for ne in range(3):
    #     path.append(ne)
    #     recur(cnt+1)
    #     path.pop()

    # 1개의 카드를 뽑는다
    # path.append(0)
    #
    #
    # # 다음 재귀 호출 (뽑은 카드 리스트 전달)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(1)
    # recur(cnt+1)
    # path.pop()
    #




#제일 처음 호출 할 때 시점
recur(0)

