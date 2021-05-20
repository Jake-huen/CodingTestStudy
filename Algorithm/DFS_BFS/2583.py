from collections import deque
m,n,k = map(int,input().split())
#가로:n 세로:m 직사각형 개수:k
square=[]
for i in range(k):
    #직사각형의 왼쪽 아래 꼭짓점, 오른쪽 위 꼭짓점
    square.append(list(map(int,input().split())))
nemo=[[0]*(m) for _ in range(n)]#각 점에 사각형 있는지 판단하는 그래프
total=[]#방들의 넓이들 저장할 배열
#print(square[0])
#(x,y) -> (x+1,y) (x,y+1) (x+1,y+1)
def check(x,y):
    nx=(x+x+1)/2
    ny=(y+y+1)/2
    for i in range(len(square)):
        if nx>=square[i][0] and nx<=square[i][2]:
            if ny>=square[i][1] and ny<=square[i][3]:
                return False
            else:
                continue
        else:
            continue
    return True
for i in range(n):
    for j in range(m):
        if check(i,j):
            nemo[i][j]=0
        else:
            nemo[i][j]=1
#print(nemo)
#m=5 n=7
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    nemo[a][b]=1
    count=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif nemo[nx][ny]==1:
                continue
            elif nemo[nx][ny]==0:
                count+=1
                nemo[nx][ny]=1
                q.append((nx,ny))
    total.append(count)
for i in range(n):
    for j in range(m):
        if nemo[i][j]==0:
            bfs(i,j)
total.sort()
print(len(total))
for i in range(len(total)):
    print(total[i],end=' ')
