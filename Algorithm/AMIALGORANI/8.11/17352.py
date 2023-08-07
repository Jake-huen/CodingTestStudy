from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 2):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
q = deque([1])
while q:
    x = q.popleft()
    visited[x] = True
    for a in graph[x]:
        if not visited[a]:
            q.append(a)
for i in range(2, n + 1):
    if not visited[i]:
        print(1, i)
        break
