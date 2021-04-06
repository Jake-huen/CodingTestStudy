# DFS 와 DFS
from collections import deque
n,m,v = map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

def dfs(v):
    print(v,end=' ')
    visited[v]=1
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)
def bfs(v):
    queue = deque([v])
    visited[v]=0
    while(queue):
        ss = queue.popleft()
        print(ss,end=' ')
        for i in range(1,n+1):
            if visited[i]==1 and graph[ss][i]==1:
                queue.append(i)
                visited[i]=0
dfs(v)
print()
bfs(v)