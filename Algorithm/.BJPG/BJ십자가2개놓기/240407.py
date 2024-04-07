n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))


def can_go(x, y, idx):
    if 0 <= x - idx and x + idx <= n - 1 and 0 <= y - idx and y + idx <= m - 1:
        if graph[x + idx][y] == '#' and graph[x - idx][y] == '#' and graph[x][y + idx] == '#' and graph[x][
            y - idx] == '#':
            return True
        else:
            return False
    return False


ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            idx = 0
            while True:
                if can_go(i, j, idx):
                    idx += 1
                else:
                    break
            for k in range(idx):
                ans.append([i, j, k])


def product_case(a, b):
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(a[2] + 1):
        for j in range(4):
            visited[a[0] + dx[j] * i][a[1] + dy[j] * i] = True
    for i in range(b[2] + 1):
        for j in range(4):
            if visited[b[0] + dx[j] * i][b[1] + dy[j] * i]:
                return False
    return True


answer = 0
for i in range(len(ans) - 1):
    for j in range(i + 1, len(ans)):
        temp = (1 + 4 * ans[i][2]) * (1 + 4 * ans[j][2])
        if temp > answer and product_case(ans[i], ans[j]):
            answer = temp
print(answer)

"""
#있는 칸에만 십자가를 놓을 수 있다
놓을 수 있는 점에서 최대로 뻗을 수 있는 것까지 구해서 경우를 모두 구한 뒤,
그 경우에서 2개를 뽑아 겹치지 않는 최대의 곱을 구함.
"""
