import sys
input = sys.stdin.readline

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
# dp[x][x][0] = 가로, dp[x][x][1] = 세로, dp[x][x][2] = 대각선
dp[0][1][0] = 1
for i in range(1, n):
    if house[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if house[i][j] == 0: # 가로
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        if house[i][j] == 0: # 세로
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if house[i][j - 1] == 0 and house[i - 1][j] == 0 and house[i][j] == 0: # 대각선
            dp[i][j][2] = dp[i - 1][j - 1][1] + dp[i - 1][j - 1][0] + dp[i - 1][j - 1][2]

print(sum(dp[n-1][n-1]))