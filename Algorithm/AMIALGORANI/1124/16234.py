from collections import deque

n, l, r = map(int, input().split())  # 땅 크기 : N*N
people = []
for i in range(n):
    people.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    q = deque()
    q.append([a, b])
    country = deque()
    country.append([a, b])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(people[nx][ny] - people[x][y]) <= r:
                    country.append([nx, ny])
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return country


day = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                country = bfs(i, j)
                if len(country) > 1:
                    sum_people = 0
                    for p in country:
                        sum_people += people[p[0]][p[1]]
                    for p in country:
                        people[p[0]][p[1]] = sum_people // len(country)
                    result += len(country)
    if result == 0:
        break
    day += 1
print(day)
