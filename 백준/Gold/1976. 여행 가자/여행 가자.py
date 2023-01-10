from collections import deque

n = int(input())  # 도시의 수
m = int(input())  # 여행계획 도시의 수
graph = []
ans = True
for _ in range(n):
    graph.append(list(map(int, input().split())))
travel_city = list(map(int, input().split()))
start = travel_city[0] - 1


def bfs(graph, start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        city = q.popleft()
        for i in range(len(graph[city])):
            if graph[city][i] == 1 and visit[i] == 0:
                visit[i] = 1
                q.append(i)


visit = [0] * n
bfs(graph, start, visit)
for city in travel_city:
    if visit[city - 1] == 0:
        ans = False
if ans:
    print("YES")
else:
    print("NO")
