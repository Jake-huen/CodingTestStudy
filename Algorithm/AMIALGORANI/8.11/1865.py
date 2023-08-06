import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):

    n, m, w = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    distance = [10001] * (n + 1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges[s].append([e, t])
        edges[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges[s].append([e, -t])


    def bellman_ford(start):
        distance[start] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in edges[j]:
                    next_node = k[0]
                    cost = k[1]
                    if distance[next_node] > distance[j] + cost:
                        distance[next_node] = distance[j] + cost
                        if i == n:
                            return True
        return False


    negative_cycle = bellman_ford(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")
