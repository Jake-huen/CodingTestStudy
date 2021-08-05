from collections import deque
import sys
input = sys.stdin.readline
q=deque()
n= int(input())
for i in range(n):
    question = input().split()
    if len(question)==2:
        order = question[0]
        number = int(question[1])
        q.append(number)
    else:
        if question[0]=='pop':
            if len(q)==0:
                print(-1)
            else:
                print(q.popleft())
        elif question[0]=='size':
            print(len(q))
        elif question[0]=='empty':
            if len(q)==0:
                print(1)
            else:print(0)
        elif question[0]=='front':
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
        elif question[0]=='back':
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])
