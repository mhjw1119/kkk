from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    que = [0] * N
    global front
    global rear
    front,rear = -1, N-1
    #
    # def enqueue (queue,n,item) :
    #
    #     queue[n-1] = item
    # def dequeue (queue) :
    #     back1 = queue[front]
    #     front += 1
    #     return back1
    # def enqueue (queue, item) :
    #     queue[rear] = item
    def ss (arr) :
        arr.deque()





    for z in range(M) :
        back = dequeue(arr)
        for i in range(N-1) :

             arr[i] = arr[i+1]

        enqueue(arr,back)

    print(f'#{test_case} {arr[0]}')