n = int(input())
t = list(map(int, input().split()))

sangsa = [[] for _ in range(n)]
for i in range(1, len(t)):
    sangsa[t[i]].append(i)

time = [0] * n


def dp(node):
    childTime = []
    for child in sangsa[node]:
        dp(child)
        childTime.append(time[child])
    if len(sangsa[node]) == 0:
        childTime.append(0)
    childTime.sort(reverse=True)
    ans = 0
    for i in range(len(childTime)):
        temp = childTime[i] + i + 1
        if temp > ans:
            ans = temp
    time[node] = ans


dp(0)
print(time[0] - 1)
