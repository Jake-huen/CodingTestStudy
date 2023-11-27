def solution(n, s, a, b, fares):
    INF = int(1e9)
    cost = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost[i][i] = 0
    for fare in fares:
        start = fare[0]
        end = fare[1]
        val = fare[2]
        cost[start][end] = val
        cost[end][start] = val
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, cost[s][i] + cost[i][a] + cost[i][b])
    return answer


print(solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
