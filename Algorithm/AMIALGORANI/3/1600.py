from collections import deque

horse_x = [-2, -1, 1, 2, -2, -1, 1, 2]
horse_y = [-1, -2, -2, -1, 1, 2, 2, 1]

monkey_x = [-1, 0, 1, 0]
monkey_y = [0, -1, 0, 1]

graph = []
k = int(input())
w, h = map(int, input().split())
for _ in range(h):
    graph.append(list(map(int, input().split())))  # 0은 평지, 1은 장애물

visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]  # 방문여부, 말처럼 여부

q = deque()
q.append([0, 0, 0])


def bfs():
    while q:
        x, y, horse = q.popleft()
        if x == h - 1 and y == w - 1:
            return visited[h - 1][w - 1][horse]
        for i in range(4):
            next_x = x + monkey_x[i]
            next_y = y + monkey_y[i]
            if 0 <= next_x < h and 0 <= next_y < w and graph[next_x][next_y] == 0:
                if not visited[next_x][next_y][horse]:
                    q.append([next_x, next_y, horse])
                    visited[next_x][next_y][horse] = visited[x][y][horse] + 1
        if horse < k:  # 말처럼 행동한적 없을때
            for i in range(8):
                next_x = x + horse_x[i]
                next_y = y + horse_y[i]

                if 0 <= next_x < h and 0 <= next_y < w and graph[next_x][next_y] == 0:
                    if not visited[next_x][next_y][horse + 1]:
                        q.append([next_x, next_y, horse + 1])
                        visited[next_x][next_y][horse + 1] = visited[x][y][horse] + 1
    return -1


print(bfs())
# print(count)
