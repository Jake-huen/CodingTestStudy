n = int(input())
t = []
s = []
p = []
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    s.append(y)
    p.append((y - x, y, x))
p.sort(key=lambda x: (x[0], x[1]))
start = p[0][0]
if start < 0:
    print(-1)
else:
    while start >= 0:
        temp = start
        for i in range(len(p)):
            temp += p[i][2]
            if temp > 24:
                start -= 1
                break
        if temp < 24:
            print(start)
            break