from collections import deque
n,m = map(int,input().split()) # map : nXn
x,y = map(int,input().split()) # 나이트 위치
graph=[[-1]*n for _ in range(n)]
ans=[]
moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
q=deque()
q.append((x-1,y-1))
graph[x-1][y-1]=0
while q:
    a,b = q.popleft()
    for move in moves:
        nx = a+move[0]
        ny = b+move[1]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==-1:
            q.append((nx,ny))
            graph[nx][ny]=graph[a][b]+1
# print(graph)
for i in range(m):
    x,y=map(int,input().split())
    ans.append(graph[x-1][y-1])
print(*ans)