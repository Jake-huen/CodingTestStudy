import sys
sys.setrecursionlimit(10000)

n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
big =0
small=10001
#graph에서 높이 최대와 최소 확인하기
for i in range(5):
    for j in range(5):
        big=max(big,graph[i][j])
        small=min(small,graph[i][j])
#건물 최대는 big, 최소는 small
def dfs(x,y,new_graph):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if new_graph[nx][ny]==0:
            new_graph[nx][ny]=1
            dfs(nx,ny,new_graph)

answer=0
for k in range(small,big+1):
    new_graph=[[0]*n for _ in range(n)]
    result=0
    #잠기는 부분을 1로, 안 잠기는 부분을 0으로
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=k:
                new_graph[i][j]=1

    for i in range(n):
        for j in range(n):
            if new_graph[i][j]==0:
                dfs(i,j,new_graph)
                result+=1
    answer = max(answer,result)

print(answer)