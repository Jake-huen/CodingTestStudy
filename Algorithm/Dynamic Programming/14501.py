n = int(input())
t = []
p = []
d = [0] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# d[i]=max(t[i]+d[i+p[i]],d[i+1]) 그 일을 하는경우,하지않고 다음날 일을 하는 경우
for i in range(n - 1, -1, -1):
    d[i] = max(t[i] + d[i + p[i]], d[i + 1])
    if i + p[i] > n:
        d[i] = d[i + 1]


print(d[0])
