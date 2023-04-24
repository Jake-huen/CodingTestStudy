def fast(s, n):
    temp = []
    for i in range(n):
        temp.append(min(ants[i], s - ants[i]))
    return max(temp)


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
    for i in range(n):
        ants.append(int(input()))
    min_time = fast(s, n)
    max_time = slow(s, n)
    print(min_time, max_time)
