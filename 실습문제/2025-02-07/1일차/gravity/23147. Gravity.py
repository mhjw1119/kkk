# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
######  결국 제일 최댓값을 구하고 그 다음 차순위 최대값을 구해서  큰값에서 차순위 큰값의 인덱스 값을 빼주면 최대 낙차다
import sys
sys.stdin = open("in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    box = list(map(int,input().split()))
    check = box.index(max(box))

    print(check)
    if check == N-1 :
        for i in range(N) :
            if i == N-1 :
                result = 0
                break

            if box[i] > box[i+1] :
                result = 1
                break

    kang_reverse = sorted(box,reverse = True)
    reversesort_max_index = max(kang_reverse)
    kang = sorted(box)
    sort_max_index = kang.index(max(kang))
    sort_min_index = kang.index(min(kang))
    result = sort_max_index - sort_min_index

    print(f'#{test_case} {result}')




    # box_max = box.index(max(box))


    # if box_max == N-1 :
    #     print('boxmax')
    #     print(box_max)
    #     for i in range(N-(N-box_max),0,-1) :
    #         if i == 0:
    #             result = 0
    #             break
    #         elif box[i-1] > box[i] :
    #             result = 1
    #         else :
    #             result =0
    #         # elif box[i-1] > box[i]:
    #         #     result =1
    #
    # else :
    #     backup = [0] * (N-(box_max + 1) )
    #     for i in range(N-(box_max + 1)) :
    #         backup[i] = box[box_max+1+i]
    #     box_max2 = backup.index(max(backup))
    #     result = (box_max2 - (box_max+1))+((N)-(box_max2+1))
    # print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
