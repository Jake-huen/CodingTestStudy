n, m, k = map(int, input().split())

dp = [[1 for _ in range(m + 1)] for _ in range(n + 1)]
# dp[i][j] : a가 i개, z가 j개로 만들 수 있는 문자열 개수
# dp[0][1] = 1
# dp[1][0] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[n][m] < k:
    print(-1)
else:
    answer = ''
    while True:
        if n == 0:
            answer += 'z' * m
            break
        if m == 0:
            answer += 'a' * n
            break
        check = dp[n - 1][m]
        if k <= check:
            answer += 'a'
            n -= 1
        else:
            answer += 'z'
            m -= 1
            k -= check
    print(answer)
