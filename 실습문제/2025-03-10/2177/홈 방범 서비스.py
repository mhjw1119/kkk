import sys
sys.stdin = open('input.txt','r')

def search (y,x) :
    for i in r


T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N) :
        for j in range(N) :
            result = max(search(i, j), result)
    print(result)