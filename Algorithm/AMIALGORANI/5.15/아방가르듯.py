def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 10
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 3
        dp[3] = 10
        temp = [0, 1, 2, 4]
        for i in range(4, n + 1):
            dp[i] = dp[i - 3] + temp[3] + dp[i - 2] + temp[2] + dp[i - 1] + temp[1]
        print(dp)
    return dp[n] % 1000000007


solution(5)
