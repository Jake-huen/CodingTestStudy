answer = []
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [0] * m
    for i in range(m):
        temp = list(map(int, input().split()))
        dp = [[0 for _ in range(2)] for _ in range(n)]  # dp[i][0] : 선택안했을때 dp[i][1] : 선택했을때
        dp[0][0] = 0
        dp[0][1] = temp[0]
        for j in range(1, n):
            dp[j][0] = max(dp[j - 1][0], dp[j - 1][1])
            dp[j][1] = dp[j - 1][0] + temp[j]
        graph[i] = max(dp[n - 1][0], dp[n - 1][1])
    # print(graph)
    ans = [[0 for _ in range(2)] for _ in range(m)]
    ans[0][0] = 0
    ans[0][1] = graph[0]
    for i in range(1, m):
        ans[i][0] = max(ans[i - 1][0], ans[i - 1][1])
        ans[i][1] = ans[i - 1][0] + graph[i]
    answer.append(max(ans[m - 1][0], ans[m - 1][1]))
for i in answer:
    print(i)
