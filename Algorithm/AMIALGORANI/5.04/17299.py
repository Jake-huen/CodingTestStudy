import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
f = {}
stack = []  # stack에는 해당하는 숫자를 넣어준다
for number in numbers:
    if number in f.keys():
        f[number] += 1
    else:
        f[number] = 1

# numbers = numbers[::-1]
ngf = [-1] * n
stack = [0]
for i in range(1, n):
    while stack and f[numbers[stack[-1]]] < f[numbers[i]]:
        ngf[stack.pop()] = numbers[i]
    stack.append(i)
print(*ngf)


