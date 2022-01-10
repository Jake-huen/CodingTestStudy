n= int(input())
connect=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)
INF = int(1e9)
parent = [INF]*(n+1)
visited = [False]*(n+1)
parent[1]=0
visited[1]=True
q=[]
temp=1
for i in connect[1]:
    parent[i]=1
    visited[i]=True
    q.append(i)
while q:
    for i in range(len(q)):
        x = q.pop()
        for j in connect[x]:
            if not visited[j]:
                parent[j]=x
                visited[j]=True
                q.append(j)
for i in range(2,n+1):
    print(parent[i])