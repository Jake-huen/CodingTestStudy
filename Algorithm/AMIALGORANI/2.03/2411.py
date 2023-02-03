from collections import deque
import sys

input = sys.stdin.readline

n, m, a, b = map(int, input().split())
item = []
block = []
for i in range(a):
    x, y = map(int, input().split())
    item.append((x - 1, y - 1))
for i in range(b):
    x, y = map(int, input().split())
    block.append((x - 1, y - 1))
item.sort(key=lambda x: (x[1], x[0]))


def bfs(a, b, x, y):
    graph = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    graph[a][b] = 1
    for i in range(a, x + 1):
        for j in range(b, y + 1):
            x1, y1 = i + 1, j
            x2, y2 = i, j + 1
            #print(i,j)
            #print("x1, y1 : ", x1, y1)
            #print("x2, y2 : ", x2, y2)
            if a <= x1 <= x and b <= y1 <= y:
                if (x1, y1) not in block:
                    #print("1번째 : ", x1, y1)
                    graph[x1][y1] += graph[i][j]
            if a <= x2 <= x and b <= y2 <= y:
                if (x2, y2) not in block:
                    #print("2번째 : ", x2, y2)
                    graph[x2][y2] += graph[i][j]
    # print(graph)
    # print()
    return graph[x][y]


ans = 1
current = [0, 0]
for i in range(a):
    x, y = item[i]
    # print(current, x, y)
    ans = ans * bfs(current[0], current[1], x, y)
    current = [x, y]
# print(current)
ans = ans * bfs(current[0], current[1], n-1, m-1)
print(ans)
