n = int(input())
stack=[]
answer=[]
cnt=1
for i in range(n):
    num=int(input())
    while num>=cnt:
        stack.append(cnt)
        answer.append('+')
        cnt+=1
    if stack[-1]==num:
        stack.pop()
        answer.append('-')
if len(stack)==0:
    for a in answer:
        print(a)
else:
    print("NO")