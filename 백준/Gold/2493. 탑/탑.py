n = int(input())
tops = list(map(int, input().split()))
ans = []
stack = [[0, tops[0]]]
for i in range(len(tops)):
    while stack:
        if stack[-1][1] > tops[i]:  # 이미 있는 값이 나보다 클 때
            ans.append(stack[-1][0] + 1)
            stack.append([i, tops[i]])
            break
        else:
            stack.pop()
    if len(stack) == 0:
        ans.append(0)
        stack.append([i, tops[i]])
print(*ans)
