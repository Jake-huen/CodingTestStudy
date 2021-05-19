from collections import deque
m,n,k = map(int,input().split())
#가로:n 세로:m 직사각형 개수:k
square=[]
for i in range(k):
    #직사각형의 왼쪽 아래 꼭짓점, 오른쪽 위 꼭짓점
    square.append(list(map(int,input().split())))
#print(square[0])
#(x,y) -> (x+1,y) (x,y+1) (x+1,y+1)
def check(x,y):
    for i in range(len(square)):
        if x>=square[i][0] and x<=square[i][2] and y>=square[i][1] and y<=square[i][3]:
            return False
        else:
            continue
    return True
q = deque()
q.append((0,0))
dx=[1,0,1]
dy=[0,1,1]
nemo=0
while q:
    x,y = q.popleft()
    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if check(nx,ny):
            q.append((nx,ny))
        else:
            break



