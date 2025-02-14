'''


받은 값에서 0부터 N까지 순회를 돈다
이 때 y를 만나면 해당 y를 n으로 바꾸고 해당 인덱스 값으로 순회를 돌며
리스트의 나머지 값들을
나눠서 0이 되면 걔네도  y를 n으로 바꾼다

'''

arr = list(input())

length = len(arr)
result = [0] * (length+1)

for i in range(1, length+1) :
    result[i] = arr[i-1]

# for i in range(1, length+1) :
#     if result[i] == 'Y' :
#         result[i] = 'N'
i = 1
count = 0
while i != (length+1) :
    if result[i] == 'Y' :
        result[i] = 'N'
        for z in range(i+1,length+1) :
            if z < length+1 :
                if z % i == 0 :
                    if result[z] == 'Y':
                        result[z] = 'N'
                    elif result[z] == 'N' :
                        result[z] = 'Y'

            else :
                break

        count += 1
    i += 1
if 'Y' in result :
    count = -1
    # print(result)
print(count)