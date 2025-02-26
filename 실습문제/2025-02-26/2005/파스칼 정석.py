import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    prev_stack = [1]

    for i in range(1, N):
        new_stack = [1]

        for j in range(len(prev_stack) - 1):
            new_stack.append(prev_stack[j] + prev_stack[j+1])

        new_stack.append(1)

        print(' '.join(map(str, new_stack)))

        prev_stack = new_stack  # 다음 반복을 위해서 이전 행을 갱신해준다.
