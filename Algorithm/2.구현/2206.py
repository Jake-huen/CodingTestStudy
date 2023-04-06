from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
dp[0][0][0] = 1  # row, col, 벽부쉈는지
q = deque()
q.append((0, 0, 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, wall = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if wall == 0 and graph[nx][ny] == '1' and dp[nx][ny][1] == 0:  # 아직 부순적 없고, 벽을 만났을때
                q.append((nx, ny, 1))
                dp[nx][ny][1] = dp[x][y][wall] + 1
            elif graph[nx][ny] == '0' and dp[nx][ny][wall] == 0:
                q.append((nx, ny, wall))
                dp[nx][ny][wall] = dp[x][y][wall] + 1

x = dp[n - 1][m - 1][0]
y = dp[n - 1][m - 1][1]
if x == 0:
    if y == 0:
        print(-1)
    else:
        print(y)
else:
    if y == 0:
        print(x)
    else:
        print(min(x, y))
