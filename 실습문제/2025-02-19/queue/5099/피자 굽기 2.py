
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    fire = [0]  * N

    for i in range(N) :
        fire[i] = [arr[i], i+1]
    M_count = N
    while len(fire) != 1 :

        for i in  range(len(fire)) :
            if len(fire) <= i :
                break
            if fire[i][0] == 0 :
                if M_count < M:
                    fire[i] = [arr[M_count], M_count+1 ]
                    M_count += 1
                else:
                    fire.pop(i)
            else:
                fire[i][0] = (fire[i][0]//2)
                if fire[i][0] == 0 :
                    if M_count < M:
                        fire[i] = [arr[M_count], M_count + 1]
                        M_count += 1
                    else :
                        fire.pop(i)

    print(f'#{test_case} {fire[0][-1]}')



