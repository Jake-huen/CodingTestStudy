n, m = map(int, input().split())
info = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    info[x].append(y)
    degree[y] += 1
answer = []
q = []
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
while q:
    q.sort(reverse=True)
    temp = q.pop()
    answer.append(temp)
    for i in info[temp]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
print(*answer)
