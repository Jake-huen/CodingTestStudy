from collections import deque

n, k = map(int, input().split())
INT = int(1e9)
d = [-1] * 100001
d[n] = 0
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(d[k])
        break
    if 0 <= x - 1 and d[x - 1] == -1:
        d[x - 1] = d[x] + 1
        q.append(x - 1)
    if 2 * x < 100001 and d[2 * x] == -1:
        d[2 * x] = d[x]
        q.append(2 * x)
    if x + 1 < 100001 and d[x + 1] == -1:
        d[x + 1] = d[x] + 1
        q.append(x + 1)

