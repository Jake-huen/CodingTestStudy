from itertools import combinations
from collections import deque

n, m, k = map(int, input().split())
costs = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
    v, w = map(int, input().split())
    graph[v - 1].append(w - 1)
    graph[w - 1].append(v - 1)
temp = [i for i in range(n)]
answers = []


def friend_friend(nodes):
    q = deque()
    answer = 0
    visited = [False for _ in range(n)]
    for node in nodes:
        q.append(node)
        answer += costs[node]
    while q:
        start = q.popleft()
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                q.append(i)
    return visited, answer


for i in range(1, n + 1):
    ways = list(combinations(temp, i))  # 친구를 고르는 모든 가지 수
    for way in ways:
        visited, answer = friend_friend(way)
        flag = True
        for k in range(n):  # 다 방문했는지 확인
            if not visited[k]:
                flag = False
        if flag:
            answers.append(answer)
if len(answers) == 0 or min(answers) > k:
    print("Oh no")
else:
    print(min(answers))
