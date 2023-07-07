from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left = numbers[:n // 2]
right = numbers[n // 2:]

answer = 0
left_cases = {}
right_cases = {}
for i in range(1, len(left) + 1):
    for x in combinations(left, i):
        if sum(x) in left_cases:
            left_cases[sum(x)] += 1
        else:
            left_cases[sum(x)] = 1
for i in range(1, len(right) + 1):
    for x in combinations(right, i):
        if sum(x) in right_cases:
            right_cases[sum(x)] += 1
        else:
            right_cases[sum(x)] = 1
# print(left_cases)
# print(right_cases)
if s in left_cases:
    answer += left_cases[s]
if s in right_cases:
    answer += right_cases[s]

for left_case in left_cases:
    if s - left_case in right_cases:
        answer += left_cases[left_case] * right_cases[s - left_case]
print(answer)
