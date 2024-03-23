# dp로 풀기

t = int(input())


def bridge(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, m + 1):
        dp[1][i] = i

    for j in range(2, n + 1):
        for k in range(j, m + 1):
            for l in range(k, j - 1, -1):
                dp[j][k] += dp[j - 1][l - 1]

    return dp[n][m]


for _ in range(t):
    n, m = map(int, input().split())
    print(bridge(n, m))

