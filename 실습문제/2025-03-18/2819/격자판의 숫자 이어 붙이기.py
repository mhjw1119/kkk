
def check ( check_list, start ):
    global check_result
    global cnt
    if len(check_list) == 7 :
        if check_list not in check_result:
            cnt += 1
            check_result.append(check_list[:])
        return

    if start >= len(num_result) :
        start = 0


    # check_list.append(num_result[start])
    # check(check_list, start+1)
    # check_list.pop()
    #
    # check(check_list,start+1)
    # i = 0
    # while 1 :
    #     check_list.append(num_result[start])
    #     if check_list.count(num_result[start]) > num_cnt[num_result[start]] :
    #         continue
    #     check(check_list, start+1 )
    #     check_list.pop()


    for i in num_result :
        check_list.append(i)
        if check_list.count(i) > num_cnt[i] :
            pass
        else:
            check(check_list, start + 1 )

        check_list.pop()
        # check(check_list)






T = int(input())

for tc in range( 1, T + 1 ):
    arr = [list(map(int, input().split())) for _ in range(4)]
    num = sum(arr, [])
    num_result = list(set(num))
    num_cnt = {}
    for i in num_result:
        num_cnt[i] = num.count(i)
    # print(num_cnt)
    check_result = []
    cnt = 0
    back_up = []
    check(back_up,0)
    print(cnt)
