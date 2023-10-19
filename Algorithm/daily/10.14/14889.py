n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(n)]
ans = int(1e9)


def dfs(l, idx):
    global ans
    if l == n // 2:
        # print(visited)
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += graph[i][j]
                elif not visited[i] and not visited[j]:
                    b += graph[i][j]
        ans = min(abs(a - b), ans)
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(l + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(ans)
