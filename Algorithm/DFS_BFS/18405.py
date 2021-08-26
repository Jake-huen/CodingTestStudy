from collections import deque
n,k = map(int,input().split())
graph=[] # n*n
for i in range(n):
    graph.append(list(map(int,input().split())))
s,u,v = map(int,input().split())
# s초 뒤에 (u,v)에 존재하는 바이러스의 종류 출력 -> 밑에서 x,y를 사용해서 u,v로 바꿈
dx=[-1,1,0,0]
dy=[0,0,1,-1]
q=deque()
for a in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==a:
                q.append((i,j))
# print(q.popleft())
for _ in range(s):
    for _ in range(len(q)):
        x,y=q.popleft()
        num = graph[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
                graph[nx][ny]=num
                q.append((nx,ny))
print(graph[u-1][v-1])