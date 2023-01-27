import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))


def minGraph():
    x = 0
    y = 0
    ans = 1001
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1:
                if graph[i][j] < ans:
                    ans = graph[i][j]
                    x = i
                    y = j
    return x, y


if r % 2 == 1:
    answer = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1)
    print(answer)
elif c % 2 == 1:
    answer = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1)
    print(answer)
else:
    low = 1000
    position = [-1, -1]
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > graph[i][j]:
                    low = graph[i][j]
                    position = [i, j]
        else:  # i % 2 == 1
            for j in range(0, c, 2):
                if low > graph[i][j]:
                    low = graph[i][j]
                    position = [i, j]

    res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xbound = 2 * (position[1] // 2) + 1
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'
        if y != r - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)

    print(res)
