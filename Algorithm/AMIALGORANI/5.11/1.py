def solution(triangle):
    tl = len(triangle)
    dp = [0] * (len(triangle))
    for i in range(tl):
        dp[i] = [0] * (i + 1)
    for i in range(tl):
        for j in range(len(triangle[i])):
            if i == 0:
                dp[i][j] = triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
    ans=0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j]>ans:
                ans=dp[i][j]
    return ans


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
