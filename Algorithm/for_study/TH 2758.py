from collections import deque
q = deque()
q.append((1,2,3))
x,y,z = q.popleft()
print(x,y,z)
