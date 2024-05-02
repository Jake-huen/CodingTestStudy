n = int(input())
graph = []
dp = [1] * (n)
for i in range(n):
    graph.append(int(input()))
# print(graph)
# 가장 긴 부분 증가 수열 / 이외 나머지만 옮겨주면 됨.
for i in range(n):
    for j in range(i):
        if graph[j] < graph[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
