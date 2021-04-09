import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx=[0,-1,-1,-1,0,1,1,1]
    dy=[1,1,0,-1,-1,-1,0,1]
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
