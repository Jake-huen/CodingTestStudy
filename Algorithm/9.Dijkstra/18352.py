import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
answer=[]

for _ in range(m):
    i,j = map(int,input().split())
    graph[i].append(j)

queue=deque()
queue.append((x,0))
visited[x]=True

while queue:
    v,dist=queue.popleft()
    if dist == k:
        answer.append(v)
    elif dist<k:
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append((i,dist+1))

if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])