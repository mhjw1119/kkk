arr = [1,2,3,4,5,6]

result = []
cnt1 = 0
def sett (cnt, ar,start):
    global cnt1
    if len(ar) == 3 :
        print(ar)
        cnt1 += 1
        return

    for i in range(start,len(arr)):
        ar.append(arr[i])
        sett(cnt+1, ar,i)
        ar.pop()




    # ar.append(arr[cnt])
    # sett(cnt+1, ar)
    # ar.pop()


sett(0,result,0)
print(cnt1)