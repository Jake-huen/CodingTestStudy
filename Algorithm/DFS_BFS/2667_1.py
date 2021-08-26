#BFS로 풀어보기
from collections import deque
n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
apt=[]
def bfs(a,b):
    q=deque([])
    q.append((a,b))
    apt_num = 1
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    while q:
        x,y=q.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==1:
                 graph[nx][ny] = 0
                 q.append((nx,ny))
                 apt_num+=1
            else:
                continue
    apt.append(apt_num)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
print(len(apt))
apt.sort()
for i in range(len(apt)):
    print(apt[i])
