from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
rx, ry, bx, by, ex, ey = 0, 0, 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx = i
            ry = j
        if graph[i][j] == "B":
            bx = i
            by = j
        if graph[i][j] == "O":
            ex = i
            ey = j


def goleft(rx, ry, bx, by, visited):
    # y가 벽을 만날때까지 움직이기
    if by < ry:  # 파란 구슬이 더 왼쪽에 있을 경우
        while by > 0:
            by -= 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#':
                by += 1
                break
        while ry > 0:
            ry -= 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#' or (rx == bx and ry == by):
                ry += 1
                break
            visited[rx][ry] = True
    else:
        while ry > 0:
            ry -= 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#':
                ry += 1
                break
            visited[rx][ry] = True
        while by > 0:
            by -= 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#' or (rx == bx and ry == by):
                by += 1
                break
    return rx, ry, bx, by


def goright(rx, ry, bx, by, visited):
    if by > ry:  # 파란 구슬이 더 오른쪽에 있을 경우
        # print("파란 구슬이 더 오른쪽")
        while by < m:
            by += 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#':
                by -= 1
                break
        while ry < m:
            ry += 1
            if graph[rx][ry] == 'O':
                # print("종료")
                return rx, ry, -1, -1
            if graph[rx][ry] == '#' or (rx == bx and ry == by):
                ry -= 1
                break
            visited[rx][ry] = True
    else:
        # print("상관 없음")
        while ry < m:
            ry += 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#':
                ry -= 1
                break
            visited[rx][ry] = True
        while by < m:
            by += 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#' or (rx == bx and ry == by):
                by -= 1
                break
    return rx, ry, bx, by


def goup(rx, ry, bx, by, visited):
    if bx < rx:  # 파란 구슬이 더 위에 있을 경우
        while bx > 0:
            bx -= 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#':
                bx += 1
                break
        while rx > 0:
            rx -= 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#' or (rx == bx and ry == by):
                rx += 1
                break
            visited[rx][ry] = True
    else:
        while rx > 0:
            rx -= 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#':
                rx += 1
                break
            visited[rx][ry] = True
        while bx > 0:
            bx -= 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#' or (rx == bx and ry == by):
                bx += 1
                break
    return rx, ry, bx, by


def godown(rx, ry, bx, by, visited):
    if bx > rx:  # 파란 구슬이 더 아래에 있을 경우
        while bx < n:
            bx += 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#':
                bx -= 1
                break
        while rx < n:
            rx += 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#' or (rx == bx and ry == by):
                rx -= 1
                break
            visited[rx][ry] = True
    else:
        while rx < n:
            rx += 1
            if graph[rx][ry] == 'O':
                return rx, ry, -1, -1
            if graph[rx][ry] == '#':
                rx -= 1
                break
            visited[rx][ry] = True
        while bx < n:
            bx += 1
            if graph[bx][by] == 'O':
                return -1, -1, -1, -1
            if graph[bx][by] == '#' or (rx == bx and ry == by):
                bx -= 1
                break
    return rx, ry, bx, by


# 실패 조건
# 1. 파란 구슬이 구멍에 빠질 경우
# 2. 빨간 구슬이랑 파란 구슬 동시에 구멍에 빠질 경우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
q.append([rx, ry, bx, by, 0])
visited = [[False] * m for _ in range(n)]
visited[rx][ry] = True
while q:
    start_rx, start_ry, start_bx, start_by, cnt = q.popleft()
    if cnt > 10:
        print(-1)
        exit(0)
    for i in range(4):
        nrx = start_rx + dx[i]
        nry = start_ry + dy[i]
        if i == 0:
            if 0 <= nrx < n and 0 <= nry < m and graph[nrx][nry] != '#':
                if not visited[nrx][nry]:
                    r1, r2, b1, b2 = goleft(start_rx, start_ry, start_bx, start_by, visited)
                    if b1 == -1 and b2 == -1:
                        if r1 == -1 and r2 == -1:
                            continue
                        else:
                            cnt += 1
                            print(cnt)
                            exit(0)
                    else:
                        visited[r1][r2] = True
                        q.append([r1, r2, b1, b2, cnt + 1])
        elif i == 1:
            if 0 <= nrx < n and 0 <= nry < m and graph[nrx][nry] != '#':
                if not visited[nrx][nry]:
                    r1, r2, b1, b2 = goright(start_rx, start_ry, start_bx, start_by, visited)
                    if b1 == -1 and b2 == -1:
                        if r1 == -1 and r2 == -1:
                            continue
                        else:
                            cnt += 1
                            print(cnt)
                            exit(0)
                    else:
                        visited[r1][r2] = True
                        q.append([r1, r2, b1, b2, cnt + 1])
        elif i == 2:
            if 0 <= nrx < n and 0 <= nry < m and graph[nrx][nry] != '#':
                if not visited[nrx][nry]:
                    r1, r2, b1, b2 = goup(start_rx, start_ry, start_bx, start_by, visited)
                    if b1 == -1 and b2 == -1:
                        if r1 == -1 and r2 == -1:
                            continue
                        else:
                            cnt += 1
                            print(cnt)
                            exit(0)
                    else:
                        visited[r1][r2] = True
                        q.append([r1, r2, b1, b2, cnt + 1])
        elif i == 3:
            if 0 <= nrx < n and 0 <= nry < m and graph[nrx][nry] != '#':
                if not visited[nrx][nry]:
                    r1, r2, b1, b2 = godown(start_rx, start_ry, start_bx, start_by, visited)
                    if b1 == -1 and b2 == -1:
                        if r1 == -1 and r2 == -1:
                            continue
                        else:
                            cnt += 1
                            print(cnt)
                            exit(0)
                    else:
                        visited[r1][r2] = True
                        q.append([r1, r2, b1, b2, cnt + 1])
print(-1)
