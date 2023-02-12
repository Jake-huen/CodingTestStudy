# n = 100 세제곱 -> 백만
n = int(input())
m = int(input())
graph = [[int(1e9) for _ in range(n)] for _ in range(n)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start - 1][end - 1] = min(cost, graph[start - 1][end - 1])
for k in range(n): # k를 기준으로
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif graph[i][j] == int(1e9):
            graph[i][j] = 0
for i in range(n):
    print(*graph[i])
