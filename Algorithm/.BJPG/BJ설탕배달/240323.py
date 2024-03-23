n = int(input())

"""
n킬로그램 배달해야함
3,5 => 최대한 적은 봉지
"""
if n<5:
    if n==3:
        print(1)
    else:
        print(-1)
else:

    dp = [-1 for _ in range(n + 1)]
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n + 1):
        if dp[i - 3] == -1 and dp[i - 5] == -1:
            dp[i] = -1
        else:
            if dp[i - 3] == -1:
                dp[i] = dp[i - 5] + 1
            elif dp[i - 5] == -1:
                dp[i] = dp[i - 3] + 1
            else:
                dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    print(dp[n])
