n = int(input())
graph=[]#지도
for _ in range(n):
    graph.append(list(map(int,input())))
#특정한 지점의 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은지점 방문
answer=[]
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1

print(result)