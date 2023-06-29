from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [False] * (v + 1)
q = deque()
q.append(1)
ans = 0
while q:
    x = q.popleft()
    visited[x] = True
    next = []
    temp = 2147483647
    for check in graph[x]:
        if not visited[check[0]]:
            if check[1] < temp:
                next = [check[0], check[1]]
                temp = check[1]
    if len(next) != 0:
        q.append(next[0])
        ans += next[1]
print(ans)
