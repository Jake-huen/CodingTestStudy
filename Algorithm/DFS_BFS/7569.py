from collections import deque
import sys
m,n,h=map(int,input().split())
#m:가로 n:세로 h:높이
tomato=[[list(map(int,sys.stdin.readline().split())) for i in range(n)] for j in range(h)]
#1:익음 0:안익음 -1:없음
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]
q=deque()
#익어 있는 것들 q에 모두 저장
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                q.append((i,j,k))

day=0
count=len(q)
while q:
    for _ in range(count):
        z,y,x = q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
                continue
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = 1
                q.append((nz, ny,nx))
            if tomato[nz][ny][nx] == -1:
                continue
    count=len(q)
    day += 1
answer=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                answer=-1
if answer!=-1:
    answer=day-1
print(answer)
# from collections import deque
# import sys
# m,n,h = map(int, sys.stdin.readline().split())
# tomato = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(h)]
# queue = deque()
# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]
#
# for i in range(h):
#   for j in range(n):
#       for k in range(m):
#        if tomato[i][j][k] == 1:
#          queue.append([i,j,k])
#
# if len(queue)==h*m*n:
#   print(0)
#   exit()
#
# while queue:
#   a,b,c = queue.popleft()
#   for i in range(6):
#     k,x,y = a+dz[i], b+dx[i], c+dy[i]
#     if 0<=k<h and 0<=x<n and 0<=y<m and tomato[k][x][y]==0:
#       queue.append([k,x,y])
#       tomato[k][x][y] = tomato[a][b][c]+1
#
# max_num = 0
# for i in range(h):
#       for j in range(n):
#             for k in range(m):
#                   if tomato[i][j][k]==0:
#                         print(-1)
#                         exit()
#                   max_num = max(max_num, tomato[i][j][k])
# print(max_num-1)