# n이 10 -> 시간제한은 0.5초 -> 5000만번
# 100 00 00 0 n7제곱 가능
# 인구 수 100 -> n 3제곱 까지 가능

from collections import deque
from itertools import combinations

n = int(input())
people = list(map(int, input().split()))  # [5,2,3,4,1,2]
graph = [[]]  # [[], [2, 4], [1, 3, 5, 6], [2, 4], [1, 3], [2], [2]]
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(sorted(temp[1:]))


def bfs(nodes):  # nodes : 지나가야할 점들
    q = deque()
    q.append(nodes[0])
    visited = [False for _ in range(n + 1)]
    while q:
        start = q.pop()
        visited[start] = True
        for node in graph[start]:  # 그래프와 연결되어 있는지 확인
            if node in nodes and not visited[node]:  # 지나가야할 점들 목록에 있는지 확인
                q.append(node)
    sum = 0
    for node in nodes:
        if not visited[node]:
            return 0, False
        else:
            sum += people[node - 1]
    return sum, True


# print(bfs((1,)))

ans = 1000
for i in range(1, n // 2 + 1):
    temp = [i + 1 for i in range(n)]
    ways = list(combinations(temp, i))
    for way in ways:
        sum1, check1 = bfs(way)
        if check1:
            temp = []
            for j in range(1, n + 1):
                if j not in way:
                    temp.append(j)
            sum2, check2 = bfs(temp)
            if check2:
                diff = abs(sum2 - sum1)
                if diff < ans:
                    ans = diff
if ans==1000:
    print(-1)
else:
    print(ans)
'''
    전체를 둘로 나누는 모든 방법
    (1) (2,3,4,5,6)
'''
