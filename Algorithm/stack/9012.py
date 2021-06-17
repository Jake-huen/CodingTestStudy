#VPS인지 아닌지 판단
def PVS(x):
    stack=[]
    for i in range(len(x)):
        if x[i]=='(':
            stack.append(x[i])
        elif x[i]==')':
            if len(stack)!=0:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
T = int(input())
for i in range(T):
    x=list(input())
    if PVS(x):
        print('YES')
    else:
        print('NO')