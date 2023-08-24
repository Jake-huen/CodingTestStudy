import heapq

n, m, x = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append([time, end])


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])  # 우선순위, 값
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if current_distance < distances[current_destination]:
            continue
        for new_distance, new_destination in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances

answer = 0
for i in range(1, n+1):
    distance = dijkstra(graph, i)[x] + dijkstra(graph, x)[i]
    if distance > answer:
        answer = distance
print(answer)
