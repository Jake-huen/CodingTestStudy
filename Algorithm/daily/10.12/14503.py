from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# d: 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
# 현재 방향 : d
graph = [] * n
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 0: 청소 안된 칸, 1: 벽이 있는 것

q = deque([[r, c, d]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph[r][c] = 2
ans = 1

while q:
    r, c, d = q[-1]
    flag = False
    for i in range(d, d - 4, -1):
        d = (i + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                ans += 1
                q.append([nx, ny, d])
                flag = True
                break
    if not flag:
        nx = r - dx[d]
        ny = c - dy[d]
        if graph[nx][ny] == 1:
            break
        else:
            q.append([nx, ny, d])

print(ans)
