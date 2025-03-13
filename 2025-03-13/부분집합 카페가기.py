arr = [ 'a', 'b', 'c','d','e']
result = []

def part (cnt,ar) :
    if cnt == len(arr) -1 :
        if len(ar) == 3 :

        return


    part(cnt,ar)
    ar.append(arr[cnt])
    part(cnt+1, ar)



part(0,result)

print(result)