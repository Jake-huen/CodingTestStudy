n = int(input())
d = []
r = [0] * n
for _ in range(n):
    d.append(int(input()))

if n==0: print(0)
elif n==1:print(d[0])
elif n==2:print(d[0]+d[1])
else:
    r[0] = d[0]
    r[1] = d[0] + d[1]
    r[2] = max(d[0] + d[2], d[1] + d[2])

    for i in range(3, n):
        r[i] = max(r[i - 2] + d[i], r[i - 3] + d[i - 1] + d[i])

    print(r[n - 1])

