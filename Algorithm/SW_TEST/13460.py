from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
map=[list(input().strip()) for _ in range(n)]
visited=[[[[False]*m for _ in range(n)]]*m for _ in range(n)]
# print(map)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()

def init():
    rx,ry,bx,by=[0]*4
    for i in range(n):
        for j in range(m):
            if map[i][j]=='R':
                rx,ry=i,j
            if map[i][j]=='B':
                bx,by=i,j
    q.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by]=True

def move(x,y,dx,dy):
    count=0
    while map[x+dx][y+dy]!='#' and map[x][y]!='O':
        x+=dx
        y+=dy
        count+=1
    return x,y,count

def bfs():
    init()
    q.poplef
