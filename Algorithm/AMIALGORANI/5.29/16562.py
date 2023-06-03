from collections import deque

n, m, k = map(int, input().split())  # 학생 수, 친구관계 수, 가지고 있는 돈
costs = list(map(int, input().split()))  # 친구별 필요한 돈
graph = [[] for _ in range(n)]

for _ in range(m):
    v, w = map(int, input().split())
    graph[v - 1].append(w - 1)
    graph[w - 1].append(v - 1)
temp = [i for i in range(n)]
answers = []
visited = [False for _ in range(n)]

def bfs(start):
    q = deque()
    members = set()
    min_node = 10000
    q.append(start)
    while q:
        x = q.popleft()
        if costs[x] < min_node:
            min_node = costs[x]
        visited[x] = True
        members.add(x)
        for node in graph[x]:
            if not visited[node]:
                q.append(node)
    return min_node
min_cost = 0
for i in range(n):
    if not visited[i]:
        min_cost += bfs(i)
if min_cost > k:
    print("Oh no")
else:
    print(min_cost)