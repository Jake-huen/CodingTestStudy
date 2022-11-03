from collections import deque
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
#벽은 한개까지 부술 수 있음.
graph=[]
for i in range(n):
    graph.append(list(map(int,list(input().strip()))))
def bfs():
    visited = [[[0] * 2 for i in range(m)] for j in range(n)]
    visited[0][0][1] = 1
    # visited는 2개 만들어서 0인 경우:벽을 뚫을 수 있는 경우, 1인 경우:벽을 뚫을 수 없는 경우
    q = deque()
    q.append((0, 0, 1))
    while q:
        x,y,w = q.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and w==1:#벽이 있고 한번도 안뚫음
                    visited[nx][ny][0]=visited[x][y][1]+1
                    q.append((nx,ny,0))#벽이제 못뚫음
                elif graph[nx][ny]==0 and visited[nx][ny][w]==0:#아직 방문안함
                    visited[nx][ny][w]=visited[x][y][w]+1
                    q.append((nx,ny,w))
    return -1
print(bfs())