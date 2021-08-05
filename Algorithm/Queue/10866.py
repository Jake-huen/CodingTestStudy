import sys
input = sys.stdin.readline
from collections import deque

q=deque()
n=int(input())
for i in range(n):
    question = input().split()
    if len(question)==2:
        order=question[0]
        number=question[1]
        if order=='push_front':
            q.appendleft(number)
        elif order=='push_back':
            q.append(number)
    else:
        if question[0]=='pop_front':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif question[0]=='pop_back':
            if q:
                print(q.pop())
            else:
                print(-1)
        elif question[0]=='size':
            print(len(q))
        elif question[0]=='empty':
            if q:
                print(0)
            else:
                print(1)
        elif question[0]=='front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif question[0]=='back':
            if q:
                print(q[-1])
            else:
                print(-1)
