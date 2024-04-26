""" 공주님의 정원
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10

2
"""
n = int(input())
flowers = []
for _ in range(n):
    temp = list(map(int, input().split()))
    flowers.append((temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]))
flowers.sort(key=lambda x: (x[0], -x[1]))
print(flowers)
start = 301
end = 0
ans = 0
while flowers:
    if start >= 1201 or start < flowers[0][0]:
        break

    for _ in range(len(flowers)):
        if start >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    start = end
    ans += 1
if start <= 1201:
    print(0)
else:
    print(ans)
