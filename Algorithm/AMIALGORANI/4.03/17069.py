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

# from collections import deque
#
# n = int(input())
# house = []
# for _ in range(n):
#     house.append(list(map(int, input().split())))
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[0][1] = 1  # row,col,가로
# q = deque()
# q.append((0, 1, 0))
# while q:
#     row, col, dir = q.popleft()
#     if dir == 0:  # 가로인 경우
#         if 0 <= col + 1 < n:  # 가로 -> 가로
#             if house[row][col + 1] == 0:
#                 q.append((row, col + 1, 0))
#                 dp[row][col + 1] += dp[row][col]
#         if 0 <= col + 1 < n and 0 <= row + 1 < n:  # 가로 -> 대각선
#             if house[row + 1][col + 1] == 0 and house[row + 1][col] == 0 and house[row][col + 1] == 0:
#                 q.append((row + 1, col + 1, 2))
#                 dp[row + 1][col + 1] += dp[row][col]
#     elif dir == 1:  # 세로인 경우
#         if 0 <= row + 1 < n:  # 세로 -> 세로
#             if house[row + 1][col] == 0:
#                 q.append((row + 1, col, 1))
#                 dp[row + 1][col] += dp[row][col]
#         if 0 <= row + 1 < n and 0 <= col + 1 < n:  # 세로 -> 대각선
#             if house[row + 1][col + 1] == 0 and house[row + 1][col] == 0 and house[row][col + 1] == 0:
#                 q.append((row + 1, col + 1, 2))
#                 dp[row + 1][col + 1] += dp[row][col]
#     elif dir == 2:  # 대각선인 경우
#         if 0 <= col + 1 < n:  # 대각선 -> 가로
#             if house[row][col + 1] == 0:
#                 q.append((row, col + 1, 0))
#                 dp[row][col + 1] += dp[row][col]
#         if 0 <= row + 1 < n:  # 대각선 -> 세로
#             if house[row + 1][col] == 0:
#                 q.append((row + 1, col, 1))
#                 dp[row + 1][col] += dp[row][col]
#         if 0 <= row + 1 < n and 0 <= col + 1 < n:  # 대각선 -> 대각선
#             if house[row + 1][col + 1] == 0 and house[row + 1][col] == 0 and house[row][col + 1] == 0:
#                 q.append((row + 1, col + 1, 2))
#                 dp[row + 1][col + 1] += dp[row][col]
# print(dp[n - 1][n - 1])
