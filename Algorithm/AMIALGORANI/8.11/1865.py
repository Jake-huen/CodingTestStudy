import sys
input = sys.stdin.readline

tc = int(input())
INF = 100001
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    wormhole = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s][e] = t
        graph[e][s] = t
    for _ in range(w):
        s, e, t = map(int, input().split())
        wormhole[s][e] = -t
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b], graph[a][k] + wormhole[k][b],
                                  wormhole[a][k] + graph[k][b], wormhole[a][k] + wormhole[k][b])
    flag = False
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b and graph[a][b] < 0:
                flag = True
    if flag:
        print("YES")
    else:
        print("NO")
