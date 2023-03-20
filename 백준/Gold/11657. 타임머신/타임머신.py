import sys

input = sys.stdin.readline


def shortcut(start):
    graph[start] = 0
    for i in range(n):  # 노드 개수만큼 반복
        for j in range(m):
            current_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if graph[current_node]!=int(1e9) and graph[next_node] > graph[current_node] + cost:
                graph[next_node] = graph[current_node] + cost
                if i == n - 1:
                    return True
    return False


n, m = map(int, input().split())
graph = [int(1e9)] * (n + 1)
edges = []
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))

if shortcut(1):
    print(-1)
else:
    for i in range(2, n + 1):
        if graph[i] == int(1e9):
            print(-1)
        else:
            print(graph[i])
