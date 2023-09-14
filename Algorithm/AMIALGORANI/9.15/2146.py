from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]


def bfs(x, y, idx):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        graph[x][y] = idx
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True


idx = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j, idx)
            idx += 1


def road(i, j, idx):
    q = deque()
    q.append((i, j))
    # print(i, j, idx)
    visited = [[-1] * n for _ in range(n)]
    visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0 and graph[nx][ny] != idx:
                    return visited[x][y]
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1


answer = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] > 1:
            ans = road(i, j, graph[i][j])
            if ans != -1:
                if ans < answer:
                    answer = ans
print(answer)
