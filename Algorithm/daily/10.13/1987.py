r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
visited = [[False for _ in range(c)] for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = set([])
q.add((0, 0, graph[0][0]))
ans = 1

while q:
    x, y, alpha = q.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in alpha:
                q.add((nx, ny, alpha + graph[nx][ny]))
                ans = max(ans, len(alpha + graph[nx][ny]))

print(ans)
