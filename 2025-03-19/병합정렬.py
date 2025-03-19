arr = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(arr1):
    if len(arr1) == 1 :
        return arr1

    mid = len(arr) // 2
    left = arr1[:mid]
    right = arr1[mid:]

    left = merge_sort(left)
    right  = merge_sort(right)

    print(left,right)
