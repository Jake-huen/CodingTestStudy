from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    check = graph[x][y]
    while q:
        x, y = q.pop()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == check:
                    q.append([nx, ny])


n = int(input())
graph = []

for i in range(n):
    graph.append(list(input()))
visited = [[False for _ in range(n)] for _ in range(n)]
ans1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j)
            ans1 += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[False for _ in range(n)] for _ in range(n)]
ans2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i, j)
            ans2 += 1

print(ans1, ans2)
