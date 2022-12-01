import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


n = int(input())
dnm = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
answer = 0

def dfs(x, y):
    # 이미 계산한 좌표면 바로 리턴
    if visited[x][y]>0:
        return visited[x][y]
    # 방문하지 않은 좌표의 기본값은 1
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if dnm[nx][ny] > dnm[x][y]: # 현재 노드부터 DFS 진행했을 때 최대로 움직일 수 있는 칸
                visited[x][y] = max(visited[x][y], dfs(nx, ny)+1)
    return visited[x][y]

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)




# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
#     dx=[-1,1,0,0]
#     dy=[0,0,-1,1]
#     graph=[[0 for _ in range(n)]]*(n)
#     while q:
#         x,y = q.pop()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<n and 0<=ny<n:
#                 if dnm[nx][ny]>dnm[x][y] and not visited[nx][ny]:
#                     q.append((nx,ny))
#                     graph[nx][ny] = graph[x][y]+1
#     answer=0
#     for i in range(n):
#         for j in range(n):
#             answer = max(answer,graph[i][j])
#     return answer
