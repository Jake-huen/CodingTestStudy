n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def first(x, y):
    temp_one = 0
    temp_two = 0
    if y + 3 < m:
        temp_one = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x][y + 3]
    if x + 3 < n:
        temp_two = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 3][y]
    return max(temp_one, temp_two)


def second(x, y):
    if x + 1 < n and y + 1 < m:
        return graph[x][y] + graph[x + 1][y] + graph[x][y + 1] + graph[x + 1][y + 1]
    else:
        return 0


def third(x, y):
    temp_one = 0
    temp_two = 0
    temp_three = 0
    temp_four = 0
    temp_five = 0
    temp_six = 0
    temp_seven = 0
    temp_eight = 0
    if x + 2 < n and y + 1 < m:
        temp_one = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 2][y + 1]
    if x + 2 < n and y - 1 > -1:
        temp_two = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 2][y - 1]
    if y + 2 < m and x - 1 > -1:
        temp_three = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x - 1][y + 2]
    if y + 2 < m and x + 1 < n:
        temp_four = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x + 1][y + 2]
    if x - 2 > -1 and y + 1 < m:
        temp_five = graph[x][y] + graph[x - 1][y] + graph[x - 2][y] + graph[x - 2][y + 1]
    if x - 2 > -1 and y - 1 > -1:
        temp_six = graph[x][y] + graph[x - 1][y] + graph[x - 2][y] + graph[x - 2][y - 1]
    if x + 1 < n and y - 2 > -1:
        temp_seven = graph[x][y] + graph[x][y - 1] + graph[x][y - 2] + graph[x + 1][y - 2]
    if x - 1 > -1 and y - 2 > -1:
        temp_eight = graph[x][y] + graph[x][y - 1] + graph[x][y - 2] + graph[x - 1][y - 2]
    return max(0, temp_one, temp_two, temp_three, temp_four, temp_five, temp_six, temp_seven, temp_eight)


def fourth(x, y):
    temp_one = 0
    temp_two = 0
    temp_three = 0
    temp_four = 0
    if x + 1 < n and y + 2 < m:
        temp_one = graph[x][y] + graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 1][y + 2]
    if x + 2 < n and y + 1 < m:
        temp_two = graph[x][y] + graph[x + 1][y] + graph[x + 1][y + 1] + graph[x + 2][y + 1]
    if x + 1 < n and y - 2 > -1:
        temp_three = graph[x][y] + graph[x][y - 1] + graph[x + 1][y - 1] + graph[x + 1][y - 2]
    if x + 2 < n and y - 1 > -1:
        temp_four = graph[x][y] + graph[x + 1][y] + graph[x + 1][y - 1] + graph[x + 2][y - 1]
    return max(temp_one, temp_two, temp_three, temp_four, 0)


def fifth(x, y):
    temp_one = 0
    temp_two = 0
    temp_three = 0
    temp_four = 0
    if x + 1 < n and y - 1 > -1 and y + 1 < m:
        temp_one = graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x + 1][y]
    if x - 1 > -1 and y + 1 < m and x + 1 < n:
        temp_two = graph[x][y] + graph[x - 1][y] + graph[x + 1][y] + graph[x][y + 1]
    if x - 1 > -1 and y - 1 > -1 and y + 1 < m:
        temp_three = graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x - 1][y]
    if x - 1 > -1 and y - 1 > -1 and x + 1 < n:
        temp_four = graph[x][y] + graph[x + 1][y] + graph[x - 1][y] + graph[x][y - 1]
    return max(temp_one, temp_two, temp_three, temp_four, 0)


ans = 0
for i in range(n):
    for j in range(m):
        temp = max(first(i, j), second(i, j), third(i, j), fourth(i, j), fifth(i, j))
        ans = max(ans, temp)
print(ans)
