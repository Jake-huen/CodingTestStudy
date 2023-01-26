# 1초 -> 1억
# n은 3이상 300이하
# n 세제곱해도 괜찮

"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
2

0 0 0 0 0 0 0
0 0 2 4 1 0 0
0 1 0 1 5 0 0
0 5 4 1 2 0 0
0 0 0 0 0 0 0

0 0 0 0 0 0 0
0 0 0 3 0 0 0
0 0 0 0 4 0 0
0 3 2 0 0 0 0
0 0 0 0 0 0 0
"""

from collections import deque

n, m = map(int, input().split())  # n,m : 행,열의 개수
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y, chunk_visited):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not chunk_visited[nx][ny] and 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                q.append((nx, ny))
                chunk_visited[nx][ny] = True


def count_chunk():  # 덩어리 개수
    chunk_visited = [[False for _ in range(m)] for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not chunk_visited[i][j]:
                bfs(i, j, chunk_visited)
                ans += 1
    return ans


def year_melting():
    graphZeroCount = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                zero_count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            zero_count += 1
                graphZeroCount.append((i, j, zero_count))
    while graphZeroCount:
        i, j, zero_count = graphZeroCount.pop()
        graph[i][j] -= zero_count
        if graph[i][j] < 0:
            graph[i][j] = 0
    # print(graph)


count = 0
while True:
    temp = count_chunk()  # 덩어리 수
    if temp >= 2: # 덩어리가 2개 이상인 경우
        print(count)
        break
    elif temp == 0: # 다 녹아버린 경우
        print(0)
        break
    else: # 덩어리가 1개인 경우
        year_melting()
        count += 1
