import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

hq = [(0, 1)]  # cost, node
cnt = 0
visited = [False] * (n + 1)
maxDist = 0
ans = 0
while cnt != n:
    curCost, curNode = heapq.heappop(hq)
    if visited[curNode]:
        continue

    cnt += 1
    visited[curNode] = True
    maxDist = max(maxDist, curCost)
    ans += curCost
    for nextNode, nextCost in graph[curNode]:
        if not visited[nextNode]:
            heapq.heappush(hq, (nextCost, nextNode))
print(ans - maxDist)
