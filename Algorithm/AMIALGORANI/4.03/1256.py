from itertools import permutations

n, m, k = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]
# dp[i][j] : a가 i개, z가 j개로 만들 수 있는 문자열 개수
dp[1][1] = 2
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

# from itertools import permutations
#
# n, m, k = map(int, input().split())
# book = []
# for i in range(n):
#     book.append('a')
# for i in range(m):
#     book.append('z')
# temp = sorted(list(set(list(permutations(book, n + m)))))
# if k > len(temp):
#     print(-1)
# else:
#     for i in range(len(temp[k - 1])):
#         print(temp[k - 1][i], end='')
