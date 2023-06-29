h, w = map(int, input().split())
graph = list(map(int, input().split()))
ans = 0
stack = []
for i in range(len(graph)):
    while stack and graph[i] > graph[stack[-1]]:
        top = stack.pop()
        distance = i - stack[-1] - 1
        waters = min(graph[i], graph[stack[-1]] - graph[top])
        ans += distance * waters
    stack.append(i)
