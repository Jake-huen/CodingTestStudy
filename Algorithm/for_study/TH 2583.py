# MXN 모눈종이
from collections import deque
m,n,k = list(map(int,input().split()))
rec=[]
for i in range(k):
    rec.append(list(map(int,input().split())))
#print(rec)
ja = [[0]*(m) for _ in range(n)]
# 중앙점으로
def check(i,j):
    x=(i+i+1)/2
    y=(j+j+1)/2
    for rec_cnt in range(k):
        if x>=rec[rec_cnt][0] and x<=rec[rec_cnt][2]:
            if y>=rec[rec_cnt][1] and y<=rec[rec_cnt][3]:
                return False
            else:
                continue
    return True

dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    for j in range(m):
        if check(i,j):
            ja[i][j]=0
        else:
            ja[i][j]=1
# print(ja)
# def dfs(x,y,count):
#     ja[x][y]=1
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx>=0 and nx<=n and ny>=0 and ny<=m:
#             if ja[nx][ny]==0:
#                 count+=1
#                 dfs(nx,ny,count)
#     return count
# all_rec=0
# each_rec=[]
# for i in range(n):
#     for j in range(m):
#         if ja[i][j]==0:
#             each_rec.append(dfs(i,j,1))
#             all_rec+=1
# print(all_rec)
# print(each_rec)
ans=[]
def bfs(a,b):
    q = deque()
    q.append((a,b))
    ja[a][b]=1
    count=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif ja[nx][ny]==1:
                continue
            elif ja[nx][ny]==0:
                count+=1
                ja[nx][ny]=1
                q.append((nx,ny))
    ans.append(count)
for i in range(n):
    for j in range(m):
        if ja[i][j]==0:
            bfs(i,j)
ans.sort()
print(len(ans))
print(*ans)

