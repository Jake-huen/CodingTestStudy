ss = list(input())
routes=[] # 알바벳 -> 숫자로 변환
for s in ss:
    routes.append(int(str(ord(s)-ord('A')+1)))
ans=0
print(routes)
stack=[]
for i in range(len(routes)):
    if routes[i] in stack:
        for j in range(len(stack)):
            if stack[j]==routes[i]:
                stack.pop(j)
                print(stack)
                ans+=len(stack)
                break
    else:
        stack.append(routes[i])
        print(stack)
print(ans)