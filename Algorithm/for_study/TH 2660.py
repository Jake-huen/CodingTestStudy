n=int(input())
friend=[[0 for i in range(n+1)]]*(n+1)
while True:
    x,y = map(int,input().split())
    print(x,y)
    if x==-1 and y==-1:
        break
    else:
        friend[x][y]=1
        friend[y][x]=1