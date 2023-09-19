n = int(input())
stack = []
idx = 0
for _ in range(n):
    order = list(input().split(' '))
    if order[0] == "type":
        stack.append(order[1])
        idx = int(order[2])
    elif order[0] == "undo":
        idx = int(order[2]) - int(order[1]) - 1
        if idx < 0:
            idx = 0
print(*stack[:idx], sep="")