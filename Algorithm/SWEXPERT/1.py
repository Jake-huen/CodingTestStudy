from collections import deque

t = int(input())
for _ in range(t):
    graph = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    r, c = map(int, input().split())
    for _ in range(r):
        graph.append(list(input()))
    q = deque()
    check = set()
    check.add(graph[0][0])  # 첫번째 여행하는 곳
    q.append((0, 0, check))
    visited = [[False for col in range(c)] for row in range(r)]
    while q:
        x, y, sou = q.pop()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny]:  # 방문하지 않은 나라일 경우
                    if graph[nx][ny] not in sou:  # 없는 기념품일 경우
                        sou.add(graph[nx][ny])
                        q.append((nx, ny, sou))
    print(len(check))