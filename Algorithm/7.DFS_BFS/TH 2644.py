n = int(input())
a,b = map(int,input().split())
m = int(input())
checked = [0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split()) #x는 y의 부모 번호
    graph[x].append(y)
    graph[y].append(x)
def dfs(me):
    for i in graph[me]:
        if checked[i]==0:
            checked[i]=checked[me]+1
            dfs(i)
dfs(a)
if checked[b]==0:
    print(-1)
else:
    print(checked[b])
