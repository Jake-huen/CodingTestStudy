from collections import deque

r, c = map(int, input().split())
graph = [] * r
for _ in range(r):
    graph.append(list(input()))
f_queue = deque()
q = deque()
f_visited = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
            f_visited[i][j] = 1
        elif graph[i][j] == 'J':
            q.append((i, j))
            visited[i][j] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while f_queue:
    x, y = f_queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if f_visited[nx][ny] == 0 and graph[nx][ny] != '#':
                f_visited[nx][ny] = f_visited[x][y] + 1
                f_queue.append((nx, ny))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == 0 and graph[nx][ny] != '#':
                if f_visited[nx][ny]!=0 and f_visited[nx][ny] <= visited[x][y] + 1:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        else:
            print(visited[x][y])
            exit(0)
print("IMPOSSIBLE")

