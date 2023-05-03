from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
f = {}
stack = [] # stack에는 해당하는 숫자를 넣어준다
for number in numbers:
    if number in f.keys():
        f[number] += 1
    else:
        f[number] = 1

numbers = numbers[::-1]
ngf = []

for number in numbers:
    if len(stack) == 0:  # 젤 처음 원소일때
        stack.append(number)
        ngf.append(-1)
    else:
        check = f[number] # 해당 숫자의 빈도 수
        q = []
        while stack:
            tt = stack.pop()
            check_in_stack = f[tt]
            q.append(tt)
            if check_in_stack > check:  # 오른쪽에 있으면서 더 큰 수
                ngf.append(tt)
                while q:
                    stack.append(q.pop())
                stack.append(number)
                break
        if len(stack) == 0:
            while q:
                stack.append(q.pop())
            stack.append(number)
            ngf.append(-1)
print(*ngf[::-1])


