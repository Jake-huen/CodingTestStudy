from collections import deque

n, m, k = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

# 동서남북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def roll_dice(dice, direction):
    n_dice = [0] * 6
    if direction == 0:  # 동쪽
        n_dice[0] = dice[3]
        n_dice[1] = dice[1]
        n_dice[2] = dice[0]
        n_dice[3] = dice[5]
        n_dice[4] = dice[4]
        n_dice[5] = dice[2]
    elif direction == 1:  # 남쪽
        n_dice[0] = dice[1]
        n_dice[1] = dice[5]
        n_dice[2] = dice[2]
        n_dice[3] = dice[3]
        n_dice[4] = dice[0]
        n_dice[5] = dice[4]
    elif direction == 2:  # 서쪽
        n_dice[0] = dice[2]
        n_dice[1] = dice[1]
        n_dice[2] = dice[5]
        n_dice[3] = dice[0]
        n_dice[4] = dice[4]
        n_dice[5] = dice[3]
    elif direction == 3:  # 북쪽
        n_dice[0] = dice[4]
        n_dice[1] = dice[0]
        n_dice[2] = dice[2]
        n_dice[3] = dice[3]
        n_dice[4] = dice[5]
        n_dice[5] = dice[1]
    return n_dice


now_dice = [1, 2, 3, 4, 5, 6]

q = deque([0, 0])
dir = 0
turn = 0
now_dice_x = 0
now_dice_y = 0
answer = 0
while turn < k:
    new_dice_x = now_dice_x + dx[dir]
    new_dice_y = now_dice_y + dy[dir]

    if new_dice_x < 0 or new_dice_y < 0 or new_dice_x >= n or new_dice_y >= m:
        dir = (dir + 2) % 4
        continue
    turn += 1
    new_dice = roll_dice(now_dice, dir)
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    q.append([new_dice_x, new_dice_y])
    visited[new_dice_x][new_dice_y] = True
    cnt = 1
    while q:
        now_x, now_y = q.popleft()

        for t in range(4):
            n_x = now_x + dx[t]
            n_y = now_y + dy[t]

            if n_x < 0 or n_y < 0 or n_x >= n or n_y >= m:
                continue
            if visited[n_x][n_y] or graph[n_x][n_y] != graph[new_dice_x][new_dice_y]:
                continue
            q.append([n_x, n_y])
            visited[n_x][n_y] = True
            cnt += 1
    answer += cnt * graph[new_dice_x][new_dice_y]
    if graph[new_dice_x][new_dice_y] < new_dice[5]:
        now_dir = (dir + 1) % 4
    elif graph[new_dice_x][new_dice_y] > new_dice[5]:
        now_dir = dir - 1
        if now_dir < 0:
            now_dir = 3
    now_dice_x = new_dice_x
    now_dice_y = new_dice_y
    now_dice = new_dice

print(answer)
