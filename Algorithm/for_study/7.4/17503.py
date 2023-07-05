from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())  # 축제가 열리는 기간, 채워야 하는 선호도의 합, 맥주 종류 수
bears = []
for i in range(k):
    v, m = map(int, input().split())  # 선호도, 도수레벨
    bears.append((v, m))
bears.sort(key=lambda x: (x[1], x[0]))  # 도수 -> 선호도 순으로 정렬

tmp = []
ans = 0
now_alchol = 0
for i in range(k):
    heappush(tmp, bears[i][0])  # 선호도
    ans += bears[i][0]
    now_alchol = bears[i][1]
