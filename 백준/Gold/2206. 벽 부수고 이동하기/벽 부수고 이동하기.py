from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs():
    q = deque()
    q.append((0, 0, 1))  # 시작x, 시작y, cnt, 벽뿌수기가능여부
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return max(visited[n - 1][m - 1])
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall == 1:  # 벽이 있지만 뚫을 수 있는 경우
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:  # 갈 수 있는 곳
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
    return -1


print(bfs())
