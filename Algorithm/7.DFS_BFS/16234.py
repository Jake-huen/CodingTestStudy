from collections import deque
n,l,r = map(int,input().split())
people=[]
for i in range(n):
    people.append(list(map(int,input().split())))
day=0
visited=[]
# print(people[0][0])
def bfs():
    q=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q.append((0,0))
    while q:
        x,y = q.popleft()
        a = people[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                temp = people[nx][ny]
                print(temp)
                if abs(a-temp)>=l and abs(a-temp)<=r:
                    q.append((nx,ny))
    print(q)
bfs()
