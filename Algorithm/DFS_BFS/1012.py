import sys
sys.setrecursionlimit(10000)
def dfs(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny]=0
            dfs(nx,ny)
    # if x<=-1 or x>=n or y<=-1 or y>=n:
    #     return False
    # if graph[x][y]==1:
    #     graph[x][y]=0
    #     dfs(x-1,y)
    #     dfs(x+1,y)
    #     dfs(x,y+1)
    #     dfs(x,y-1)
    #     return True
    # return False
t = int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    result=0
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                result+=1
    print(result)
