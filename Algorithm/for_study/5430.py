from collections import deque

t = int(input())


def AC(p, q):
    rc = 0
    for i in range(len(p)):
        if p[i] == 'D':
            if len(q) == 0:
                return "error"
            else:
                if rc % 2 == 0:
                    q.popleft()
                elif rc % 2 == 1:
                    q.pop()
        elif p[i] == 'R':
            rc += 1
    if rc % 2 == 1:
        q.reverse()
    # q = ''.join(map(str, q))
    return "[" + ",".join(q) + "]"


for _ in range(t):
    p = list(input())
    n = int(input())
    x = input()[1:-1].split(",")
    q = deque(x)
    if n == 0:
        q = []
    print(AC(p, q))
