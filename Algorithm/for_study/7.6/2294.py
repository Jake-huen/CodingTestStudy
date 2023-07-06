import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [sys.maxsize] * (k + 1)
dp[0] = 0
for i in range(k + 1):
    for coin in coins:
        if coin < i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
        elif coin == i:
            dp[i] = min(dp[i], 1)
if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
