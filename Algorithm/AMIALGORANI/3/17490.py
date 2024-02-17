from collections import deque

n, m, k = map(int, input().split())  # 강의동의 수, 공사구간의 수, 돌의 수
s = list(map(int, input().split()))
gongsa = [[False for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    gongsa.append([x - 1, y - 1])
if m <= 1:
    print("YES")
    exit(0)
group = []
visited = [False] * (n)


def bfs(x):
    q = deque([x])
    global visited
    visited[x] = True
    tmp = [x]
    while q:
        cur = q.popleft()
        for i in range(n):
            if gongsa[cur][i] or gongsa[i][cur]:
                continue
            elif not visited[i]:
                q.append(i)
                visited[i] = True
                tmp.append(i)
    return tmp


for i in range(n):
    if not visited[i]:
        group.append(bfs(i))
print(group)
