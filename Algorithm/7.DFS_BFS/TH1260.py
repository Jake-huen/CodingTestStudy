from collections import deque

n,m,v = map(int,input().split())
visited = [False]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

def dfs(start):
    print(start,end=' ')
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i]=True
def bfs(start):
    q = deque([start])
    visited[start]=True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
dfs(v)
visited = [False]*(n+1)
print()
bfs(v)