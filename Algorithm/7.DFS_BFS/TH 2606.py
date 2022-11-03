n = int(input()) # 컴퓨터의 수
m = int(input())
graph = [[] for _ in range(n+1)]
num=0
visited = [False]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(start):
    global num
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            num+=1
dfs(1)
print(num)