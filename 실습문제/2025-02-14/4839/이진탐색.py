'''

먼저 중간값을 찾고 그 값을 찾아야하는 값과 비교해서 작으면 다음 중간값을 찾고 아래 값을 찾는다


'''



import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P,A,B = map(int,input().split())
    Awin = 0
    Bwin = 0
    # while Awin ==1 or Bwin == 1 :
    #     i = 1
    #     c = (i+P)/2
    #     c1 = (i+P)/2
    #
    #     if P > c :
    #         for i in range()

    def check (i,r,p,count=0) :
        if