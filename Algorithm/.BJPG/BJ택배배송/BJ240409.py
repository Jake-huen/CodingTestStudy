import heapq
import sys
"""
1에 위치 -> N까지
다익스트라 -> 우선순위 큐 사용
"""


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for new_node, new_dist in graph[node]:
            temp = dist + new_dist
            if temp < distance[new_node]:
                distance[new_node] = temp
                heapq.heappush(q, (temp, new_node))


n, m = map(int, input().split())  # n개의 헛간, m개의 양방향 길
graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)
for _ in range(m):
    a_i, b_i, c_i = map(int, input().split())
    graph[a_i].append((b_i, c_i))
    graph[b_i].append((a_i, c_i))

dijkstra(1)
print(distance[n])
