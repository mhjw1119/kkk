# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# 최대값의 인덱스 값이 맨 오른쪽이면  오른쪽부터 순회해서 n-1이 n보다 클 때
# 만약 정렬 전 가장 최대 값이
# 아 그냥 순회 돌면서 해당 인덱스의 값보다 n+1 큰 인덱스 값이 자기 자신보다 크면 되는구나?

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    box = list(map(int,input().split()))
    box_max_list = [0] * N
    box_max_index = [0] * N
    box_result = [0] * N

    for i in range(N) :
        count = 0
        space = 0
        num = 0
        if i == N-1 :
            break
        if box[i] > box[i+1] :

            for x in range(i+1,N):
                if x-1 == N-1 :
                    break
                elif box[i] <= box[x] :
                    for z in range(x, N):
                        if z == N - 1:
                            break
                        if box[x] > box[z+1]:
                            space += 1
                        else :
                            break
                    # num = x
                    break
                else:
                    count += 1

        box_max_list[i] = count + space
    result = max(box_max_list)
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
