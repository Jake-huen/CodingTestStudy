"""
자기 지역 n이 주어졌을 때, n에서 각 지역에 거리를 알아야함.
"""

n, m, r = map(int, input().split())  # 지역 개수, 수색 범위, 길의 개수
t = list(map(int, input().split()))
item_graph = [[] for _ in range(n)]

distance = [[10000001 for _ in range(n)] for _ in range(n)]

# 본인 자신은 거리 0
for i in range(n):
    for j in range(n):
        if i == j:
            distance[i][j] = 0
            distance[j][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())  # 지역번호, 지역번호, 길의 길이
    item_graph[a - 1].append([b - 1, l])
    item_graph[b - 1].append([a - 1, l])
    distance[a - 1][b - 1] = l
    distance[b - 1][a - 1] = l

for i in range(n):  # 경유지
    for j in range(n):  # 출발지
        for k in range(n):  # 도착지
            if distance[j][i] + distance[i][k] < distance[j][k]:
                distance[j][k] = distance[j][i] + distance[i][k]
# print(distance)
result = 0
for i in range(n):
    ans = 0
    for j in range(n):
        if distance[i][j] <= m:
            ans += t[j]
    result = max(result, ans)
print(result)
