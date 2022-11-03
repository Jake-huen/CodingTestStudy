s=list(input())
stack=[]
answer=0
temp=1
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
        temp=temp*2
    elif s[i]=='[':
        stack.append(s[i])
        temp=temp*3
    elif s[i]==')':
        if not stack or stack[-1]!='(':
            answer=0
            break
        if s[i-1]=='(':
            answer+=temp
        stack.pop()
        temp = temp//2
    elif s[i]==']':
        if not stack or stack[-1]!='[':
            answer=0
            break
        if s[i-1]=='[':
            answer+=temp
        stack.pop()
        temp = temp//3
if stack:
    print(0)
else:
    print(answer)
# (()
# (

# s=list(input())
# stack=[]
# answer=0
# temp=1
# for i in range(len(s)):
#     if s[i]=='(':
#         stack.append(s[i])
#         temp=temp*2
#     elif s[i]=='[':
#         stack.append(s[i])
#         temp=temp*3
#     elif s[i]==')':
#         check = stack.pop()
#         if check=='(':
#             answer+=temp
#         else:
#             answer=0
#             break
#         temp = temp//2
#         print(answer, temp)
#     elif s[i]==']':
#         check = stack.pop()
#         if check=='[':
#             answer+=temp
#         else:
#             answer=0
#             break
#         temp=temp//3
#         print(answer, temp)
# print(answer)
