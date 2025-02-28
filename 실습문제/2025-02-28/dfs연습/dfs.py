arr = [1, 2, 3]
check = [0] * len(arr)
result = []

def dfs ( depth, sel):
    if depth == len(arr):
        sub = [arr[i] for i in range(len(arr)) if sel[i]]
        result.append(sub)
        return

    # if depth == len(arr) :
    #     for i in range(len(arr)) :
    #         if sel[i] == 1 :
    #             sub = arr[i]
    #             result.append(sub)
    #     print(result)
    #     return

    sel[depth] = 0
    dfs(depth7676+1, sel)

    sel[depth] = 1
    dfs(depth+1, sel)

dfs(0,check)
print(result)






