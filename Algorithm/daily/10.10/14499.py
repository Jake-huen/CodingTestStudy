n, m, x, y, k = map(int, input().split())
graph = [] * n
dice = [0] * 7
for i in range(n):
    graph.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
idx = 1  # 현재 주사위 윗면
left = 4  # 왼쪽
right = 3  # 오른쪽
up = 2  # 위
down = 5  # 아래
opp = 6  # 반대면
dice_number = [idx, left, right, up, down, opp]
for order in orders:
    order = order - 1
    nx = x + dx[order]
    ny = y + dy[order]
    if 0 <= nx < n and 0 <= ny < m:
        idx = dice_number[0]
        left = dice_number[1]
        right = dice_number[2]
        up = dice_number[3]
        down = dice_number[4]
        opp = dice_number[5]
        if order == 0:  # 동
            dice_number = [left, opp, idx, up, down, right]
        elif order == 1:  # 서
            dice_number = [right, idx, opp, up, down, left]
        elif order == 2:  # 북
            dice_number = [down, left, right, idx, opp, up]
        elif order == 3:  # 남
            dice_number = [up, left, right, opp, idx, down]
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[dice_number[5]]
        else:
            dice[dice_number[5]] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[dice_number[0]])
        x = nx
        y = ny
