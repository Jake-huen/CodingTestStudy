from collections import deque

m, n = map(int, input().split())  # 가로 m 세로 n
graph = []
for _ in range(n):
    graph.append(list(input()))
wall = [[-1 for _ in range(m)] for _ in range(n)]
wall[0][0] = 0
q = deque([])
q.append([0, 0])
while q:
    x, y = q.popleft()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if wall[nx][ny] == -1:  # 한번도 방문 안함
                if graph[nx][ny] == '0':
                    wall[nx][ny] = wall[x][y]
                    q.appendleft([nx, ny])
                else:
                    wall[nx][ny] = wall[x][y] + 1
                    q.append([nx, ny])
print(wall)
print(wall[n - 1][m - 1])
