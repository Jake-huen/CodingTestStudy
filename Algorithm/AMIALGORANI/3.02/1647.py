# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]  # 모든 도로의 가중치
# for i in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c
#
#
# def prim(graph_list):
#     visited_set = set()
#     visited_set.add(graph_list[0])
#     distance = 0
#     ans = []
#     cnt = len(graph_list)
#
#     for _ in range(cnt - 1):
#         min_dist = 1e9
#         next_node = -1
#         for node in visited_set:
#             for j in range(len(graph_list)):
#                 if graph_list[j] not in visited_set and 0 < graph[node][graph_list[j]] < min_dist:
#                     min_dist = graph[node][graph_list[j]]
#                     next_node = graph_list[j]
#         distance += min_dist
#         ans.append(min_dist)
#         visited_set.add(next_node)
#     return distance,ans
#
#
# temp = [idx for idx in range(1, n + 1)]
# answers = []
# distance,ans = prim(temp)
# print(distance - max(ans))

import sys, heapq

input = sys.stdin.readline

# 인접 리스트 생성
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 프림 알고리즘 진행
hq = [(0, 1)]
cnt = 0
visit = [False] * (n + 1)
maxDist, total = 0, 0
while cnt != n:
    dist, node = heapq.heappop(hq)
    print(dist, node)
    if visit[node]:
        continue
    cnt += 1
    visit[node] = True
    maxDist = max(maxDist, dist)
    total += dist
    for nextNode, nextDist in graph[node]:
        if not visit[nextNode]:
            heapq.heappush(hq, (nextDist, nextNode))
print(total - maxDist)
