from collections import deque
m,n=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
bback=[[-1]*m for _ in range(n)]#가중치
dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]#상하좌우

q=deque()
q.append((0,0))
bback[0][0]=0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if bback[nx][ny]==-1:
            if graph[nx][ny]==0:
                bback[nx][ny]=bback[x][y]
                q.appendleft((nx,ny))
            elif graph[nx][ny]==1:
                bback[nx][ny]=bback[x][y]+1
                q.append((nx,ny))
print(bback[n-1][m-1])