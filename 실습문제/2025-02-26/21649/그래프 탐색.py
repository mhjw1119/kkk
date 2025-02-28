# import sys
# sys.stdin = open('input.txt')
def dfs(v, N):
    visited = [0] * (N + 1)
    stack = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            print(v)
        for w in adj[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return stack
T = 1
for tc in range(1, T+1):
    V, E = map(int,input().split())
    graph = list(map(int,input().split()))
    adj = [[] for i in range(V+1)]
    check = [[0] for i in range(7)]
    for i in range(0,len(graph),2):
        adj[graph[i]].append(graph[i+1])
        adj[graph[i+1]].append(graph[i])


    print(dfs(1,E))