arr = [1,2,3]
real = []
t = []

def part(start, result):
    global real
    if start == len(arr) :
        real.append(result[:])
        return

    #
    part(start+1,result)
    # for i in range(3) :
    #     if arr[start] not in result :
    #         result.append(arr[start])
    #         part(start+1,result)
    #         result.pop()
    result.append(arr[start])
    part(start + 1, result)
    result.pop()



part(0,t)

print(real)
