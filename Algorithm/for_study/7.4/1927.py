from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())
tmp = []
for i in range(n):
    x = int(input())
    if x > 0:
        heappush(tmp, x)
    elif x == 0:
        if tmp:
            print(heappop(tmp))
        else:
            print(0)


