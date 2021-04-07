n = int(input())
m= int(input())
computer=[]
visited=[False]*(n+1)

for i in range(m):
    computer.append(list(map(int,input().split())))

def dfs(computer,v,visited):
    visited[v]=True
    for i in range(m):
        x=computer[i][0]
        y=computer[i][1]
        if not visited[y] and x==v:
            dfs(computer,y,visited)
        if not visited[x] and y==v:
            dfs(computer,x,visited)
dfs(computer,1,visited)
answer=0
for i in range(1,n+1):
    if visited[i]:
        answer+=1
print(answer-1)
