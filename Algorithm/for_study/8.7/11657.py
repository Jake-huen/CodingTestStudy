import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 도시의 개수, 버스 노선의 개수
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def bellman_ford(start):
    distance[start] = 0
    for repeat in range(n):
        for i in range(1, n + 1):
            for next, cost in graph[i]:
                if distance[i] != INF and cost + distance[i] < distance[next]:  # i를 거쳐서 가는게 곧바로 next로 가는것보다 더 짧다면
                    distance[next] = cost + distance[i]
                    if repeat == n - 1:
                        return True
    return False


negative_road = bellman_ford(1)
if negative_road:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
