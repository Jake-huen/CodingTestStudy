from collections import deque
from itertools import combinations
n,m=map(int,input().split())
graph=[]
copy_graph=[[0]*(m) for _ in range(n)]
answer=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
def copy():
    for i in range(n):
        for j in range(m):
            copy_graph[i][j]=graph[i][j]
def bfs():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif copy_graph[nx][ny]==2 or copy_graph[nx][ny]==1:
                continue
            elif copy_graph[nx][ny]==0:
                copy_graph[nx][ny]=2
                q.append((nx,ny))
def count():
    result=0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==0:
                result+=1
    answer.append(result)
arr = []
wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            arr.append((i, j))
wall = list(combinations(arr, 3))
for i in range(len(wall)):
    copy()
    for j in range(3):
        x, y = wall[i][j]
        copy_graph[x][y]=1
    bfs()
    count()
print(max(answer))

# 벽 3개를 설치하는 모든 경우의 수를 생각해야 한다.
# 가능한 모든 경우의 수를 계산, 안전 영역을 계산할 때 DFS나 BFS를 적절히 이용