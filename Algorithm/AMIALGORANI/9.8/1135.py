n = int(input())
t = list(map(int, input().split()))
sangsa = [[] for _ in range(n)]
for i in range(1, n):
    sangsa[t[i]].append(i)
time = [0] * n


def dp(node):
    childTime = []
    for child in sangsa[node]:
        dp(child)
        childTime.append(time[child])
    if not sangsa[node]:
        childTime.append(0)
    childTime.sort(reverse=True)
    need_time = [childTime[i] + i + 1 for i in range(len(childTime))]
    time[node] = max(need_time)


dp(0)
print(time[0] - 1)
