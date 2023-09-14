n = int(input())
stack = []
for _ in range(n):
    order = list(input())
    if order[0] == "type":
        stack.append((order[1], order[2]))
    elif order[0] == "undo":
        
