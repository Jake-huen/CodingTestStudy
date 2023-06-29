h, w = map(int, input().split())
graph = list(map(int, input().split()))
ans = 0
for i in range(1, w - 1):
    left_max = max(graph[:i])
    right_max = max(graph[i + 1:])
    temp = min(left_max, right_max)
    if graph[i] < temp:
        ans += temp - graph[i]
print(ans)
