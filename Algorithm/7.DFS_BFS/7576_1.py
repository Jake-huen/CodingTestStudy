from collections import deque
m,n = map(int,input().split())
#graph[n][m]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(a,b):
    q=deque()
    q.append((a,b))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    day = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==0:
                q.append((nx,ny))
        day += 1
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i,j)
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit(0)
# print(day)
