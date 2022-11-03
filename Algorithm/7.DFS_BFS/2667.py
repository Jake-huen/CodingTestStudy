n = int(input())
graph=[]#지도
apt=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        cnt+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
cnt=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            apt.append(cnt)
            cnt =0
apt.sort()
print(len(apt))
for i in range(len(apt)):
    print(apt[i])