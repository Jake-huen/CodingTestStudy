n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input())))
for _ in range(n):
    b.append(list(map(int, input())))


def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1
        if a == b:
            break
if a != b:
    print(-1)
else:
    print(cnt)
