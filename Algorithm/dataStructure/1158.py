#(n,k) - 요세푸스 순열
from collections import deque
n,k = map(int,input().split())
answer = []
q1=deque([])
for i in range(n):
    q1.append(i+1)
for _ in range(n):
    for _ in range(k-1):
        num = q1.popleft()
        q1.append(num)
    num = q1.popleft()
    answer.append(num)
print("<",end='')
for i in range(n-1):
    print(answer[i],end=', ')
print(answer[n-1],end='>')