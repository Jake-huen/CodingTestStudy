from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
board=[list(input().strip()) for _ in range(n)]
visited=[[[False]*m for _ in range(n)]*m for _ in range(n)]
# print(map)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q = deque()
# BFS 알고리즘은 queue와 while을 사용
# DFS 알고리즘은 stack과 재귀 함수 사용

# 빨간 구슬, 파란 구슬 2개가 동시에 움직이므로 각 2개의 구슬 x,y좌표를 visited 배열에
# 4차원으로 선언하고 False로 초기화

def init():
    rx,ry,bx,by = [0]*4 # 초기화 0,0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R': #board에 빨간 구슬이라면 좌표 값 저장
                rx,ry = i,j
            elif board[i][j]=='B': #board에 파란 구슬이라면 좌표 값 저장
                bx,by = i,j
    # print(rx,ry,bx,by)
    q.append((rx,ry,bx,by,1)) #위치정보와 depth
    visited[rx][ry][bx][by]=True

def move(x,y,dx,dy):
    count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍일 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x+=dx
        y+=dy
        count +=1
    return x,y,count

def bfs():
    init()
    while q:
        rx,ry,bx,by,depth = q.popleft()
        if depth >10:
            break
        for i in range(4):
            next_rx,next_ry,r_count = move(rx,ry,dx[i],dy[i])
            next_bx,next_by,b_count = move(bx,by,dx[i],dy[i])
            if board[next_bx][next_by]=='O':
                continue
            if board[next_rx][next_ry]=='O':
                print(1)
                return
            if next_rx == next_bx and next_ry==next_by:
                if r_count>b_count:
                    next_rx-=dx[i]
                    next_ry-=dy[i]
                else:
                    next_bx-=dx[i]
                    next_by-=dy[i]
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by]=True
                q.append((next_rx,next_ry,next_bx,next_by,depth+1))
    print(0)
bfs()