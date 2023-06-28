from collections import defaultdict

n, d, k, c = map(int, input().split())
graph = []
for i in range(n):
    graph.append(int(input()))
graph.extend(graph)
di = defaultdict(int)
start_pointer = 0
end_pointer = 0
ans = 0
di[c] += 1
while end_pointer < k:
    di[graph[end_pointer]] += 1
    end_pointer += 1
while end_pointer < len(graph):
    di[graph[start_pointer]] -= 1
    if di[graph[start_pointer]] == 0:
        del di[graph[start_pointer]]
    di[graph[end_pointer]] += 1
    start_pointer += 1
    end_pointer += 1
    ans = max(ans, len(di))
print(ans)
