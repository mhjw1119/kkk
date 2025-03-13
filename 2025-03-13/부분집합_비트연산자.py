arr = [ 'a', 'b', 'c','d','e']

def part (ta):
    sub_set = []
    global cnt
    for i in range(len(arr)):
        if ta & 0x1 :
        # if ta & 0x1 and arr[i] not in sub_set:
            sub_set.append(arr[i])

        ta >>= 1
    result.append(sub_set)

    # if len(sub_set) == 3:
    #     result.append(sub_set)
    #     cnt += 1
    return
result = []
cnt = 0
for target in range(1<<len(arr)):
    part(target)
    # if back >= 2 :
    #     result.append(back)
print(cnt, result)

