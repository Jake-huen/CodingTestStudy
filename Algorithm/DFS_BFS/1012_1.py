from collections import deque
def bfs(a,b):
    q=deque([])
    q.append((a,b))
    graph[a][b]=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    bechu = 0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=0
t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    total_num = 0
    for i in range(k):
        x,y = map(int,input().split())
        graph[y][x]=1
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)
                total_num+=1
    print(total_num)