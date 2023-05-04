n = int(input())
t = []
s = []
p = []
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    s.append(y)
    p.append((x, y))
p.sort(key=lambda x: (x[1]))
time = 0
while 1:
    temp = time
    for t, s in p:
        if temp + t <= s:
            temp += t
        else:
            print(time - 1) # 현재 이 시작시간이 안되는 거니까
            exit()
    time += 1