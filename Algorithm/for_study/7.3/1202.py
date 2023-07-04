from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jems = []
bags = []
for i in range(n):
    m, v = map(int, input().split())
    jems.append((m, v)) # 무게,

for i in range(k):
    bags.append(int(input()))
jems.sort()
bags.sort()
tmp = []
ans = 0
for bag in bags:
    while jems and bag >= jems[0][0]:
        heappush(tmp, -heappop(jems)[1])
    # print(bag, tmp)
    if tmp:
        ans -= heappop(tmp)
    elif not jems:
        break
print(ans)
