'''
for 문으로 각 자리를 다 돌면서
해당 위치에서 시작해서 7자리 숫자를 만든다
걍 체크 리스트가 없으면 됨

'''

def check ( y, x , check_list):
    global result_list
    global cnt
    if len(check_list) == 7 :
        result_list.add(str(check_list))
        return


    for dy, dx in [0,1],[1,0],[0,-1],[-1, 0] :
        ny = y + dy
        nx = x + dx
        if -1< ny < 4 and -1 < nx < 4 :
            check_list.append(arr[ny][nx])
            check(ny,nx,check_list)
            check_list.pop()




T = int(input())

for tc in range( 1, T + 1 ):
    arr = [list(map(int, input().split())) for _ in range(4)]
    backup = []
    result_list = set()
    cnt = 0
    for i in range(4):
        for j in range(4):
            check(i,j,backup)
    print(f'#{tc} {len(result_list)}')
