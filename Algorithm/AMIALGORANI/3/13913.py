from collections import deque

n, k = map(int, input().split())
q = deque()
q.append([n, [n]])
visited = [False] * (200001)
visited[n] = True
if n > k:
    print(n - k)
    for x in range(n, k - 1, -1):
        print(x, end=" ")
    exit(0)
while q:
    x, proc = q.popleft()
    if x == k:
        print(len(proc) - 1)
        print(*proc)
        break
    arr = [x - 1, x + 1, x * 2]
    for a in arr:
        if 0 <= a <= 100000 and not visited[a]:
            visited[a] = True
            r = proc + [a]
            q.append([a, r])

# 걷기 : x-1 x+1 순간이동 : 2*x
# 가장 빠른시간
# 어떻게 이동해야 하는지
