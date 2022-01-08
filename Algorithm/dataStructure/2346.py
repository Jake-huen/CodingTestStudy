# from collections import deque
# n = int(input())
# q = deque(enumerate(map(int,input().split())))
# ans=[]
#
# while q:
#     idx,num = q.popleft()
#     ans.append(idx+1)
#     if num>0:
#         q.rotate(-(num-1))
#     elif num<90:
#         q.rotate(-num)
# print(' '.join(map(str,ans)))
from collections import deque

n=int(input())
s=list(map(int,input().split()))
start=0
index=[x for x in range(1,n+1)]
answer=[]
temp = s.pop(start)
answer.append(index.pop(start))

while s:
    if temp<0:
        start = (start+temp)%len(s)
    else:
        start=(start+temp-1)%len(s)
    temp = s.pop(start)
    answer.append(index.pop(start))
for i in answer:
    print(i,end=' ')

