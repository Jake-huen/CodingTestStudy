from collections import deque
n,m,v = map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
def dfs(v):
    print(v,end=' ')
    visited[v] = True
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]==1:
            dfs(i)

def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        x = q.popleft()
        print(x,end=' ')
        for i in range(1,n+1):
            if not visited[i] and graph[x][i]==1:
                q.append(i)
                visited[i]=True
dfs(v)
visited=[False]*(n+1)
print()
bfs(v)