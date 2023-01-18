import sys

input = sys.stdin.readline

n, k = map(int, input().split())
stack = []
number = list(input().rstrip())  # \n

for i in range(n):
    while stack and stack[-1] < number[i] and k > 0:
        stack.pop()
        k -= 1
    stack.append(number[i])
print(''.join(stack[:len(stack) - k]))
