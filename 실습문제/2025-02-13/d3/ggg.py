# 회문1


for t in range(1, 11):
    n = int(input())
    string_grid = [input() for _ in range(8)]
    cnt = 0
    # 행 문자열 중에 palindrome이 있는지 여부
    for row_string in string_grid:
        for start_idx in range(8 - n + 1):
            for explore_idx in range(n):
                if row_string[start_idx + explore_idx] != row_string[start_idx + (n - 1) - explore_idx]:
                    break
            else:
                cnt += 1

    # 열로 탐색 했을 때 palindrome이 있는지 여부
    for col_string in zip(*string_grid):
        for start_idx in range(8 - n + 1):
            for explore_idx in range(n):
                if col_string[start_idx + explore_idx] != col_string[start_idx + (n - 1) - explore_idx]:
                    break
            else:
                cnt += 1

    print(f'#{t} {cnt}')