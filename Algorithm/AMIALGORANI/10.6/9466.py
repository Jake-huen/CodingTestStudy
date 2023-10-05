import sys
t = int(input())
sys.setrecursionlimit(1000000)

def dfs(x):
    global result
    visited[x] = True
    team.append(x)
    next_node = graph[x]
    if not visited[next_node]:
        dfs(next_node)
    else:
        if next_node in team:
            result += team[team.index(next_node):]
            return

for i in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []
    for i in range(1, n+1):
        team = []
        dfs(i)
    result = list(set(result))
    print(n-len(result))
