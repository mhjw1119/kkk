# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = int(input())
    a =0
    b = 0
    c = 0
    d = 0
    e = 0

    def aa (A,count) :

        if A/2 - int(A/2) != 0 :
            return A, count

        else :
            count += 1
            return aa(A/2,count)

    def bb (A,count) :

        if A/3 - int(A/3) != 0 :

            return A, count
        else :
            count += 1

            return bb(A/3,count)

    def cc (A,count) :

        if A/5 - int(A/5) != 0 :
            return A, count
        else :
            count += 1
            return cc(A/5,count)

    def dd (A,count) :

        if A/7 - int(A/7) != 0 :
            return A, count
        else :
            count += 1
            return dd(A/7,count)

    def ee (A,count) :

        if A/11 - int(A/11) != 0 :
            return A, count
        else :
            count += 1
            return ee(A/11,count)
    result_arr,result_a = aa(arr,a)

    result_arr, result_b = bb(result_arr, b)

    result_arr, result_c = cc(result_arr, c)
    result_arr, result_d = dd(result_arr, d)
    result_arr, result_e = ee(result_arr, e)

    print(f'#{test_case} {result_a} {result_b} {result_c} {result_d} {result_e}')
    # print(ee(dd(cc(bb(aa(arr,a))))))