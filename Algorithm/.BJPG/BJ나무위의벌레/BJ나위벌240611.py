from collections import deque

n = int(input())
fruit = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())  # 연결되어 있는 간선
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(start):
    q = deque([])
    q.append([start, fruit[start]])
    global visited
    visited[start] = True
    ans = fruit[start]
    while q:
        x, score = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                tmp = score + fruit[node]
                ans = max(ans, tmp)
                q.append([node, tmp])
                visited[node] = True
    return ans


visited = [False] * n
answer = 0
start = 0
for i in range(n):
    if not visited[i]:
        score = bfs(i)
        if score > answer:
            start = i
            answer = score
print(answer, start)