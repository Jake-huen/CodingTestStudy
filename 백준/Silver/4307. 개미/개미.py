def fast(s, n):
    mid = s // 2
    temp = []
    for i in range(n):
        temp.append(abs(ants[i] - mid))
    return mid - min(temp)


def slow(s, n):
    temp = []
    for i in range(n):
        temp.append(min(s - ants[i], ants[i]))
    return s - min(temp)

import sys
input = sys.stdin.readline
t = int(input())
answer = []
for _ in range(t):
    s, n = map(int, input().split())  # 막대의 길이, 개미의 수
    ants = []
    min_time = 0
    max_time = 0
    for i in range(n):
        ants.append(int(input()))
    for ant in ants:
        min_time = max(min_time, min(ant, s - ant))
        max_time = max(max_time, ant, s - ant)
    print(min_time, max_time)
