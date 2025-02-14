
dump = int(input())
box = list(map(int, input().split()))

'''

for문으로 최고점과 최저점을 찾는다. >> 최고점과 최저점이 같을 경우 걍 맨 왼쪽것을 택한다
최고점에서 -1하고 최저점에는 +1을한다.
덤프가 0일때까지 반복한다. 이 때 이미 최고점이랑 최저점이 같거나 최고점이 1크다면 
그냥 브레이크 하고 둘의 높이 차를 반환한다.


'''
high = 0   # 최고점
low = 0    # 최저점

while dump != 0:   #덤프가 0일때까지 반복
    if high == low or high == low + 1: # 최고점과 최저점이 같거나 최고점이 1크면 중단
        result = box[high] - box[low]
        break
    high = box[0]           #일단 최고점 최저점 첫번째 값으로 설정
    low = box[0]
    for i in range(len(box)):
        if box[i] < low:         ## 만약 i가 최고점이나 최저점보다 작거나 크면 바꾸기
            low = i
        elif box[i] == low or box[i] == high:
            continue
        elif box[i] > high:
            high = i
    result = box[high] - box[low]
print(result)



