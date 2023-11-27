import heapq


def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF

    def dijkstra(start):
        dist = [INF for _ in range(n + 1)]
        dist[start] = 0
        q = []
        heapq.heappush(q, [dist[start], start])
        while q:
            cur_dist, node = heapq.heappop(q)
            for tmp_node, tmp_dist in cost[node]:
                if dist[tmp_node] > cur_dist + tmp_dist:
                    dist[tmp_node] = cur_dist + tmp_dist
                    heapq.heappush(q, [dist[tmp_node], tmp_node])
        return dist

    cost = [[] for _ in range(n + 1)]
    for start, end, val in fares:
        cost[start].append((end, val))
        cost[end].append((start, val))

    dist = []
    for i in range(n + 1):
        dist.append(dijkstra(i))
    # print(dist)
    for i in range(1, n+1):
        answer = min(dist[s][i] + dist[i][a] + dist[i][b], answer)
    return answer


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
