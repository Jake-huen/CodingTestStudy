from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)
dp = [-1] * 100001
dp[n] = 0
while q:
    node = q.popleft()
    if node == k:
        print(dp[k])
        break
    if 0 <= node - 1 and dp[node - 1] == -1:
        dp[node - 1] = dp[node] + 1
        q.append(node - 1)
    if 0 <= node * 2 <= 100000 and dp[node * 2] == -1:
        dp[node * 2] = dp[node]
        q.append(node * 2)
    if 0 <= node + 1 <= 100000 and dp[node + 1] == -1:
        dp[node + 1] = dp[node] + 1
        q.append(node + 1)

