import sys

input = sys.stdin.readline
import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
answer = 0
if n == 1:
    print(0)
else:
    for i in range(n - 1):
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        temp = int(temp1 + temp2)
        answer += temp
        heapq.heappush(cards, temp)
    print(answer)
