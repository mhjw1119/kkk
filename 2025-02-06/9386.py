for test_case in range(1, 4):
    length = int(input())
    num = list(map(int, input()))
    print(num)
    max_result = 0
    for i in range(len(num)):
        count = 0
        count_list = []

        if num[i] == 1:
            # print(num[i])
            for x in range(i + 1, len(num)):
                if num[x] == 0:
                    break
                else:
                    count += 1
        if max_result < count:
            max_result = count

    for i in range(len(count_list)):
        if count_list[i] > max_result:
            max_result = count_list[i]

    print(f'result : {max_result + 1}')