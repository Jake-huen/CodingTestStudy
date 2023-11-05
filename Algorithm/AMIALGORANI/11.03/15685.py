n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    dir = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(dir) - 1, -1, -1):
            tmp.append((dir[i] + 1) % 4)
        for i in range(len(tmp)):
            dir.append(tmp[i])

    for i in dir:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny


ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            ans += 1

print(ans)
