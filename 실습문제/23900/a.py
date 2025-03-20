from collections import deque

def check(N, M):
    if N == M:
        return 0

    visited = [False] * (1000001)  # 방문 여부 체크 (0부터 1000000까지)
    queue = deque([(N, 0)])  # (현재 숫자, 횟수)
    visited[N] = True

    while queue:
        num, cnt = queue.popleft()

        # 가능한 모든 연산을 수행하여 큐에 추가
        for next_num in (num * 2, num - 10, num + 1, num - 1):
            if 0 <= next_num <= 1000000 and not visited[next_num]:
                if next_num == M:
                    return cnt + 1
                visited[next_num] = True
                queue.append((next_num, cnt + 1))

    return -1  # 목표에 도달할 수 없으면 -1을 반환

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = check(N, M)
    print(f'#{tc} {result}')
