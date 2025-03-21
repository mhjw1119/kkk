import heapq


def dijkstra(graph, start):
    # 각 정점에 대한 최소 거리 초기화
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # 우선순위 큐: (거리, 정점)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면 무시
        if current_distance > distances[current_vertex]:
            continue

        # 인접 노드들에 대해 거리 갱신
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 거리 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 그래프 예시 (인접 리스트 형식)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# 다익스트라 알고리즘 실행
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"최단 거리 (시작점 {start_vertex} 기준): {distances}")
