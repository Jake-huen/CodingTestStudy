from collections import deque

n, m = map(int, input().split())
way = [[] for _ in range(n + 1)]
child = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    way[a].append(b)
    child[b] += 1
q = []
for i in range(1, n + 1):
    if child[i] == 0:
        q.append(i)
answer = []
while q:
    q.sort(reverse=True)
    start = q.pop()
    for i in way[start]:
        child[i] -= 1
        if child[i] == 0:
            q.append(i)
    answer.append(start)
print(*answer)
