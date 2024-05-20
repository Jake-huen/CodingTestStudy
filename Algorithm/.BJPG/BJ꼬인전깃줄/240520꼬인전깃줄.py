n = int(input())
lines = list(map(int, input().split()))
dp = [0] * n
key = lines[0]
for i in range(1, n):
    if lines[i] > key:
        key = lines[i]
        dp[i] = dp[i - 1] + 1
    else:
        key = lines[i]
        dp[i] = 0
result = n - max(dp) - 1
dp = [0] * n
for i in range(1, n):
    if lines[i] < key:
        key = lines[i]
        dp[i] = dp[i - 1] + 1
    else:
        key = lines[i]
        dp[i] = 0
result = min(result, n - max(dp) - 1)
print(result)
