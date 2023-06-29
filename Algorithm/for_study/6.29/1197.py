# 크루스칼 알고리즘

# v, e = map(int, input().split())
# graph = []
# for i in range(e):
#     a, b, c = map(int, input().split())
#     graph.append((a, b, c))
# graph.sort(key=lambda x: x[2])
#
# parent = [i for i in range(v + 1)]
#
#
# def find_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# answer = 0
# for a, b, cost in graph:
#     if find_parent(a) != find_parent(b):
#         union_parent(a, b)
#         answer += cost
#
# print(answer)

# 프림 알고리즘
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [False] * (v + 1)
for i in range(len(graph)):
    graph[i].sort(key=lambda x: x[1])
q = [[0, 1]]  # 가중치, 노드
ans = 0
cnt = 0
while cnt < v:
    cost, node = heappop(q)
    if not visited[node]:
        visited[node] = True
        ans += cost
        cnt += 1
        for u, w in graph[node]:
            heappush(q, [w, u])
print(ans)
