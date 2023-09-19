from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)  # 앞에 달린 노드 수
for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(2, temp[0] + 1):
        degree[temp[i]] += 1
        graph[temp[i - 1]].append(temp[i])

q = deque()
visited = [False] * (n + 1)
for i in range(1, len(degree)):
    if degree[i] == 0:
        q.append(i)
        visited[i] = True
ans = []
while q:
    x = q.popleft()
    visited[x] = True
    ans.append(x)
    for child in graph[x]:
        degree[child] -= 1
    for i in range(1, len(degree)):
        if degree[i] == 0 and not visited[i]:
            q.append(i)
            visited[i] = True
for i in range(1, len(degree)):
    if degree[i] !=0:
        print(0)
else:
    print(*ans)
