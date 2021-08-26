from collections import deque
n = int(input()) #컴퓨터 수
m = int(input()) #연결 수
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y]=graph[y][x]=1
def bfs(v):
    q = deque([v])
    visited[v]=True
    while q:
        x = q.popleft()
        for i in range(1,n+1):
            if not visited[i] and graph[x][i]==1:
                q.append(i)
                visited[i]=True
num=0
bfs(1)
for i in range(1,n+1):
    if visited[i]:
        num+=1
print(num-1)