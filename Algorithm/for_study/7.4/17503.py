from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 축제가 열리는 기간, 채워야 하는 선호도의 합, 맥주 종류 수
for i in range(k):
    v, c = map(int, input().split()) # 선호도, 도수레벨


