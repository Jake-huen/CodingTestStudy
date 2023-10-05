from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx, ry, bx, by, ex, ey = 0, 0, 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx = i
            ry = j
        if graph[i][j] == "B":
            bx = i
            by = j
        if graph[i][j] == "O":
            ex = i
            ey = j
q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    cnt = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


while q:
    rx, ry, bx, by, ans = q.popleft()
    if ans > 10:
        print(-1)
        exit(0)
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
        nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
        if graph[nbx][nby] != 'O':
            if graph[nrx][nry] == 'O':
                print(ans)
                exit(0)
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append([nrx, nry, nbx, nby, ans + 1])
print(-1)