from bisect import bisect_left

n = int(input())
lines = list(map(int, input().split()))
dp = [1]
x = [lines[0]]

for i in range(1, len(lines)):
    if lines[i] > x[-1]:
        dp.append(dp[-1] + 1)
        x.append(lines[i])
    else:
        idx = bisect_left(x, lines[i])
        x[idx] = lines[i]

print(n - max(dp))
