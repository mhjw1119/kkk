
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    max_box_size = N // 2

    min_diff = float('inf')
    possible = False  # 포장 가능 여부

    for i in range(1, N - 1):
        for j in range(i + 1, N):
            small = carrots[:i]
            medium = carrots[i:j]
            large = carrots[j:]

            # 조건 (3) 비어있는 상자가 있으면 안 된다.
            if len(small) == 0 or len(medium) == 0 or len(large) == 0:
                continue

            # 조건 (4) 한 상자에 N//2개 초과 금지
            if len(small) > max_box_size or len(medium) > max_box_size or len(large) > max_box_size:
                continue

            # 조건 (5) 같은 크기의 당근은 같은 상자에 있어야 한다.
            if len(set(small)) != len(small) or len(set(medium)) != len(medium) or len(set(large)) != len(large):
                continue

            max_count = max(len(small), len(medium), len(large))
            min_count = min(len(small), len(medium), len(large))
            diff = max_count - min_count

            if diff < min_diff:
                min_diff = diff
                possible = True

    if possible:
        print(f"#{tc} {min_diff}")
    else:
        print(f"#{tc} -1")