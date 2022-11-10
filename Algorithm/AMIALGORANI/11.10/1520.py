from heapq import heappush,heappop
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph=[]
visited=[[0 for _ in range(n)] for _ in range(m)] # DP

for _ in range(m):
    graph.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=[(0,0,0)]
visited[0][0]=1

while q:
    count,x,y = heappop(q)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if not 0<=nx<m or not 0<=ny<n:
            continue
        if graph[nx][ny]>=graph[x][y]:
            continue
        if visited[nx][ny]==0: #방문 안했으면 heapq에 추가해줌
            heappush(q, (-graph[nx][ny], nx, ny)) # 더 값 높은 곳 방문하기
        visited[nx][ny] += visited[x][y] #방문한 곳, 방문안한곳 둘 다 더해주기

print(visited[m-1][n-1])