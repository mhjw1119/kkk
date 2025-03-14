import sys
sys.stdin = open('input.txt', 'r')

def check(ar) :
    for c in range(8) :
        # if -1< c < 7 :
        if ar[c+2] >= 1 and ar[c] >= 1 and ar[c+1] >= 1 :
            return 1

        if ar[c] >= 3 :
            return 1
        # if -1< c < 6 :
        #     if ar[c-1] >= 1 and ar[c] >= 1 and ar[c+1] >= 1 :
        #         return 1
    return 0




T = int(input())


for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    cnt = [0] * 10
    cnt2 = [0] * 10
    user1_result = 0
    user2_result = 0
    result = 0
    for i in range(0,12,2):
        cnt[arr[i]] += 1

        user1_result = check(cnt)

        if user1_result == 1 :
            result = 1
            break

        cnt2[arr[i + 1]] += 1

        user2_result = check(cnt2)

        if user2_result == 1 :
            result = 2
            break
        #
        # if user2_result == 1 and user1_result == 1:
        #     break

    print(f'#{tc} {result}')