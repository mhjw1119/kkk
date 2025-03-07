# secret_code = 1004
# print(7070 ^ secret_code)

print( 1 << 1)
print( 1 << 2)
print( 1 >> 1)
print( 1 >> 2)
print( 8 >> 1)




arr = [ 1, 2 , 3 , 4]

for i in range( 1 << len(arr)) :      # 2 4 6 8
    for idx in range(len(arr)) :
        if i & (1 << idx) :             # 2 8 16 32
            print(arr[idx], end="")
    print()


