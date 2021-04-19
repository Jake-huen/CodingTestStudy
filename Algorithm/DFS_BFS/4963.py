import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx=[0,-1,-1,-1,0,1,1,1]
    dy=[1,1,0,-1,-1,-1,0,1]
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=h or ny<0 or ny>=w:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny]=0
            dfs(nx,ny)

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    graph=[]
    result=0
    for i in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                dfs(i,j)
                result+=1
    print(result)

