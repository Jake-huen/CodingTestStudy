from collections import deque
from itertools import combinations
n,m = map(int,input().split())
graph=[]
copy_graph=[[0]*m for i in range(n)]
answer=[]
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int,input().split())))
#브루트포스로 1로 만들곳 2개 선택
#bfs로 감염지역 싹 덮고
#for문으로 안전 영역 확인
#그래프를 원상태로 돌리기
def bfs():
    queue=deque()
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append((i, j)) #바이러스 위치한 곳은 큐에 넣기
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif copy_graph[nx][ny]==1 or copy_graph[nx][ny]==2:
                continue
            elif copy_graph[nx][ny]==0:
                copy_graph[nx][ny]=2
                queue.append((nx,ny))

def safe():
    result=0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==0:
                result+=1
    answer.append(result)

def copy():
    for i in range(n):
        for j in range(m):
            copy_graph[i][j]=graph[i][j]
arr=[]
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            arr.append((i,j))
ll=list(combinations(arr, 3))
for i in range(len(ll)):
    copy()
    for j in range(3):
        x,y=ll[i][j]
        copy_graph[x][y]=1
    bfs()
    safe()
print(max(answer))
