from collections import deque

row, col = map(int, input().split())  # 세로, 가로
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def total_cheese(graph):
    cnt = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                cnt += 1
    return cnt


def isCheese(a, b):  # 해당 칸이 제일 겉의 치즈인지 파악
    q = deque()
    q.append([a, b])
    visited = [[False] * col for _ in range(row)]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        graph[nx][ny] = 0
                        cnt += 1  # 겉의 치즈 개수
    return cnt


time = 0
left_cheese = []
left_cheese.append(total_cheese(graph))
while True:
    cheese = total_cheese(graph)
    time += 1
    left_cheese.append(cheese - isCheese(0, 0))
    if left_cheese[-1] == 0:
        break
print(time)
print(left_cheese[-2])
