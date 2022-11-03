string = list(input())

stack=[]
temp =1
answer=0
for i in range(len(string)):
    if string[i]=='(':
        stack.append(string[i])
        temp=temp*2
    elif string[i]=='[':
        stack.append(string[i])
        temp=temp*3
    elif string[i] == ')':
        if string[i-1]=='(':
            answer+=temp
        if len(stack)==0:
            answer=0
            break
        if stack[-1]=='[':
            answer=0
            break
        temp = temp//2
        stack.pop()
    elif string[i] == ']':
        if string[i-1]=='[':
            answer+=temp
        if len(stack)==0:
            answer=0
            break
        if stack[-1]=='(':
            answer=0
            break
        temp = temp//3
        stack.pop()
if len(stack)==0:
    answer=0
print(answer)