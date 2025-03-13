import sys
sys.stdin = open('input.txt','r')


T = int(input())


for tc in range(1,T+1):

    N, M = map(int,input().split())
    box = list(map(int,input().split()))
    car = list(map(int,input().split()))
    result = 0
    car_max = 0
    box_max = sum(box)
    box.sort(reverse=True)
    car.sort()
    check = [0] * len(box)
    for car_idx in car:
        car_max = 0
        if result >= box_max :
            break
        for j in range(N):
            if car_idx >= box[j] and car_max < box[j] and check[j] != 1:
                car_max = box[j]
                check[j] = 1
        result += car_max

    print(f'#{tc} {result}')
