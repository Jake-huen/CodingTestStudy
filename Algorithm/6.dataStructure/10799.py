s=input()
stack=[]
answer=0
# '('가 들어오는 경우 -> 쇠파이프 1개가 새로 시작하거나, 레이저인 경우
# ')'가 들어오는 경우 -> 쇠파이프 1개가 끝나거나, 레이저인 경우
for i in range(len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        if s[i-1]=='(':
            stack.pop()
            answer+=len(stack)
        elif s[i-1]==')':
            stack.pop()
            answer+=1
print(answer)