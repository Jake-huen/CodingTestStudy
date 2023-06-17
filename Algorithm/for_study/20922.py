n, k = map(int, input().split())
a = list(map(int, input().split()))
size = max(a)
d = [0] * (size + 1)
answer = 0
temp = 0
for i in range(len(a)):
    d[a[i]] += 1
    if d[a[i]] > k:
        answer = max(answer, temp)
        d = [0] * (size + 1)
        temp = 1
    else:
        temp += 1
print(answer)

# start도 기록하고, 마지막도 기록해야할듯