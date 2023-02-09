# 세 명이 한 지점에서 모였을 때 걸린 시간이 최소
from collections import deque

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))  # 처음 미로
akdang = []
for _ in range(3):
    x, y = map(int, input().split())
    akdang.append([x - 1, y - 1])  # 처음 악당들 위치


# row가 X, col이 Y

def possible_graph(start):
    q = deque()
    q.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    new_graph = [[-1 for _ in range(c)] for _ in range(r)]  # 출발지에서 목표지까지의 거리
    new_graph[start[0]][start[1]] = 0
    while q:
        start_x, start_y = q.popleft()
        for idx in range(4):
            nx = start_x + dx[idx]
            ny = start_y + dy[idx]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '0' and new_graph[nx][ny] == -1:  # 지나갈 수 있는 길이고 아직 방문하지 않은 곳
                    q.append([nx, ny])
                    new_graph[nx][ny] = new_graph[start_x][start_y] + 1
    return new_graph


first = possible_graph(akdang[0])
second = possible_graph(akdang[1])
third = possible_graph(akdang[2])

answer = []
for i in range(r):
    for j in range(c):
        if first[i][j] > -1 and second[i][j] > -1 and third[i][j] > -1:  # 전부 다 일단 방문한 곳
            answer.append(max(first[i][j], second[i][j], third[i][j]))

if len(answer) == 0:
    print(-1)
else:
    ans = min(answer)
    ans2 = 0  # ans와 같은 개수
    for temp in answer:
        if temp == ans:
            ans2 += 1
    print(ans)
    print(ans2)

'''
5 6
011110
100000
100000
110000
110110
1 1
2 2
3 3
'''
