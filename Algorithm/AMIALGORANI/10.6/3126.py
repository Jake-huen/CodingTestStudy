import math


def move(cx, cy, dir, k):
    next_dir = (dir + k) % 8
    if next_dir == 0:
        return cx - 1, cy, next_dir
    elif next_dir == 1:
        return cx - 1, cy - 1, next_dir
    elif next_dir == 2:
        return cx, cy - 1, next_dir
    elif next_dir == 3:
        return cx + 1, cy - 1, next_dir
    elif next_dir == 4:
        return cx + 1, cy, next_dir
    elif next_dir == 5:
        return cx + 1, cy + 1, next_dir
    elif next_dir == 6:
        return cx, cy + 1, next_dir
    elif next_dir == 7:
        return cx - 1, cy + 1, next_dir


def get_distance(mx, my, bx, by):
    mx = float(mx)
    my = float(my)
    bx = float(bx)
    by = float(by)
    return math.sqrt(abs(mx - bx) ** 2 + abs(my - by) ** 2)


mx, my, bx, by = map(int, input().split())
n = int(input())
orders = list(input())
ways = []
for i in range(n):
    for j in range(0, 8):
        temp = orders.copy()
        if j != temp[i]:
            temp[i] = str(j)
            ways.append(temp)
ans = int(1e9)
for way in ways:
    x, y, dir = mx, my, 0
    for i in range(len(way)):
        x, y, dir = move(x, y, dir, int(way[i]))
    temp = get_distance(x, y, bx, by)
    print(x,y, temp)
#     if temp < ans:
#         ans = temp
# print(ans)
