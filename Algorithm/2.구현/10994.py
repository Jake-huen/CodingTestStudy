def star(n, idx):
    if n == 1:
        graph[idx][idx] = "*"
        return
    l = 4 * n - 3
    for i in range(idx, l + idx):
        # 위 아래
        graph[idx][i] = "*"
        graph[idx + l - 1][i] = "*"
        # 양 옆
        graph[i][idx] = "*"
        graph[i][idx + l - 1] = "*"

    return star(n - 1, idx + 2)


n = int(input())
graph = [[' ' for _ in range(4 * n - 1)] for _ in range(4 * n - 3)]
print(graph)
star(n, 0)
row = 4 * n - 3
for i in range(row):
    for j in range(row):
        print(graph[i][j], end="")
    print()
