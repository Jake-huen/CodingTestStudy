from collections import deque
m,n = map(int,input().split())
tomato=[]
for i in range(n):
    tomato.append(list(map(int,input().split())))

queue=deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i,j))

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if tomato[nx][ny]==0:
            tomato[nx][ny]=1
            queue.append((nx, ny))
        if tomato[nx][ny] == -1:
            continue