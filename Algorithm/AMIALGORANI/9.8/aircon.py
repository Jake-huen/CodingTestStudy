def solution(temperature, t1, t2, a, b, onboard):
    temperature = temperature + 10
    t1 = t1 + 10
    t2 = t2 + 10

    dp = [[int(1e9)] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    for i in range(1, len(onboard)):
        if onboard[i] == 1:
            start = t1
            end = t2
        else:
            start = min(t1, temperature)
            end = max(t2, temperature)
        for j in range(start, end + 1):
            x = dp[i - 1][j - 1] if j - 1 >= 0 else int(1e9)
            y = dp[i - 1][j + 1] if j + 1 <= 50 else int(1e9)
            if j < temperature:
                dp[i][j] = min(x, y + a, dp[i - 1][j] + b)
            elif j > temperature:
                dp[i][j] = min(x + a, y, dp[i - 1][j] + b)
            elif j == temperature:
                dp[i][j] = min(x, y, dp[i - 1][j])
        if i == len(onboard) - 1:
            return min(dp[len(onboard) - 1])


print(solution(28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]))
