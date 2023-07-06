from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left = numbers[:n // 2]
right = numbers[n // 2:]

answer = 0
left_cases = []
right_cases = []
for i in range(1, n // 2 + 1):
    for x in combinations(left, i):
        tmp = sum(x)
        left_cases.append(tmp)
        if tmp == s:
            answer += 1
for i in range(1, n // 2 + 1):
    for x in combinations(right, i):
        tmp = sum(x)
        right_cases.append(tmp)
        if tmp == s:
            answer += 1
left_cases.sort()
right_cases.sort()

for left_case in left_cases:
    for right_case in right_cases:
        if left_case + right_case == s:
            answer += 1
print(answer)
