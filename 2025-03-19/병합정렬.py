arr = [69, 10, 30, 2, 16, 8, 31, 22]

def merge(left, right ):
    result = [0] * ( len(left) + len(right))
    l,r = 0, 0

    while l < len(left) and r < len(right) :
        if left[l] > right[r] :
            result [ l + r ] = right[r]
            r += 1
        else:
            result [ l + r ] = left[l]
            l += 1

    while l < len(left) :
        result[l+r] = left[l]
        l += 1
    while r < len(right) :
        result[l+r] = left[r]
        r += 1

    return result




def merge_sort(arr1):
    if len(arr1) == 1 :
        return arr1

    mid = len(arr1) // 2
    left1 = arr1[:mid]
    right1 = arr1[mid:]

    left1_list = merge_sort(left1)
    right1_list  = merge_sort(right1)
    # print(left, right)

    merged_list = merge(left1_list,right1_list)

    return merged_list
result1 = merge_sort(arr)

print(result1)
