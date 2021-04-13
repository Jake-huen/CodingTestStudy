from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
# 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않음
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i, j))
day = 0
count = len(queue)
while queue:
    for i in range(count):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                queue.append((nx, ny))
            if tomato[nx][ny] == -1:
                continue
    day+=1
    count=len(queue)
answer=0
for i in range(n):
    for j in range(m):
        if tomato[i][j]==0:
            answer=-1
if answer!=-1:
    answer=day-1

print(answer)