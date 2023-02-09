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

def possible_graph(start):
    q = deque()
    q.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    new_graph = [[-1 for _ in range(c)] for _ in range(r)]  # 출발지에서 목표지까지의 거리
    new_graph[start[0]][start[1]] = 0
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '0' and new_graph[nx][ny] == -1:  # 지나갈 수 있는 길이고 아직 방문하지 않은 곳
                    q.append([nx, ny])
                    new_graph[nx][ny] = new_graph[x][y] + 1
    return new_graph


first = possible_graph(akdang[0])
second = possible_graph(akdang[1])
third = possible_graph(akdang[2])
print(first)
print(second)
print(third)
answer = []
for i in range(r):
    for j in range(c):
        if first[i][j] != -1 and second[i][j] != -1 and third[i][j] != -1:  # 전부 다 일단 방문한 곳
            answer.append(max(first[i][j], second[i][j], third[i][j]))
print(answer)
if len(answer) == 0:
    print(-1)
else:
    ans = min(answer)
    ans2 = 0 # ans와 같은 개수
    for temp in answer:
        if temp == ans:
            ans2 += 1
    print(min(answer))
    print(ans2)

