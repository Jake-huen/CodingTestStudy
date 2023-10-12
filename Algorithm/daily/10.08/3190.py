from collections import deque

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    row, col = map(int, input().split())
    graph[row - 1][col - 1] = 2
L = int(input())
direction = []
temp = 0
for _ in range(L):
    x, l = input().split()
    direction.append([int(x) - temp, l])
    temp = int(x)
#print(direction)
direction.append([n, 'S'])
snake = deque([[0, 0]])
dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]
idx = 0
ans = 0
for time, dir in direction:
    for i in range(time):
        ans += 1
        head_x, head_y = snake[-1]  # 뱀의 머리
        nx = dd[idx][0] + head_x
        ny = dd[idx][1] + head_y
        #print("nx : ", nx, "ny : ", ny)
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            print(ans)
            exit(0)
        elif graph[nx][ny] == 1:
            print(ans)
            exit(0)
        else:
            snake.append([nx, ny])
        if graph[nx][ny] != 2:
            x, y = snake.popleft()
            graph[x][y] = 0
        graph[nx][ny] = 1
        #print(snake)
    if dir == 'D':
        idx = (idx + 1) % 4
    elif dir == 'L':
        idx -= 1
        if idx < 0:
            idx = 3
    elif dir == 'S':
        continue
    #print(ans)
