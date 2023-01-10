# 4
# 3 5 2 7
n = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [-1] * n
for i in range(n):
    if len(stack) == 0:
        stack.append([numbers[i], i])
        # print(stack)
    elif numbers[i] < stack[-1][0]:
        stack.append([numbers[i], i])
        # print(stack)
    else:
        while stack and numbers[i] > stack[-1][0]:
            value, index = stack.pop()
            answer[index] = numbers[i]
        stack.append([numbers[i],i])
        # print(stack)
print(*answer)
