from collections import deque,defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
hacking = [0]*(n+1)

graph = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split()) # b->a possible
    graph[b].append(a)

for i in range(1,n+1):
    visited = [False] * (n + 1)
    visited[i]=True
    q=deque()
    q.append(i)
    while q:
        x = q.popleft()
        for j in graph[x]:
            if not visited[j]:
                q.append(j)
                visited[j]=True
                hacking[i]+=1
# print(hacking)
max_ans = max(hacking)
answer=[]
for i in range(1,n+1):
    if hacking[i]==max_ans:
        print(i,end=' ')