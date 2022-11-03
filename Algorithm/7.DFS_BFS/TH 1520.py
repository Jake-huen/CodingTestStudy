m,n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited=[[-1]*n for _ in range(m)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1
    if visited[x][y]!=-1:
        return visited[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<m and ny>=0 and ny<n:
            if graph[nx][ny]<graph[x][y]:
                visited[x][y]+=dfs[nx][ny]
    return visited[x][y]
print(dfs(0,0))
