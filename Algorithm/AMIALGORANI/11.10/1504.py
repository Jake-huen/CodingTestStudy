import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())  # a번 -> b번 양방향 길 존재, 거리 c
    graph[a].append([c, b])
    graph[b].append([c, a])
v1, v2 = map(int, input().split())  # 반드시 지나야하는 정점
INF = int(1e9)
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [distance[start], start])
    while q:
        c_dist, c_node = heapq.heappop(q)
        if distance[c_node] < c_dist:
            continue
        for n_dist, n_node in graph[c_node]:
            temp = c_dist + n_dist
            if temp < distance[n_node]:
                distance[n_node] = temp
                heapq.heappush(q, [temp, n_node])


dijkstra(1)
s1, s2 = distance[v1], distance[v2]  # 각각 1->v1, 1->v2
distance = [INF] * (n + 1)
dijkstra(v1)
a1, a2 = distance[v2], distance[n]  # v1->v2, v1->n
distance = [INF] * (n + 1)
dijkstra(v2)
b1, b2 = distance[v1], distance[n]  # v2->v1, v2->n
answer = min(s1 + a1 + b2, s2 + b1 + a2)
if answer >= INF:
    print(-1)
else:
    print(answer)

"""
1번에서 N번 정점으로 최단거리 이동
조건
1. 임의로 주어진 두 정점은 반드시 통과해야한다
2. 한번 통과했던 정점, 간선 모두 다시 이동 가능하다.
3. 무조건 최단거리
방법
1 -> v1 -> v2 -> N
1 -> v2 -> v1 -> N 
"""
