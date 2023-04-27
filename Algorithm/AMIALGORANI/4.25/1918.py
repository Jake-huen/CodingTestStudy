n = list(input())
ans = ''
stack = []
for i in range(len(n)):
    if n[i].isalpha():  # 알파벳이면 그냥 ans에 더해주기
        ans += n[i]
    else:
        if n[i] == '(':
            stack.append(n[i])
        elif n[i] == '*' or n[i] == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '-'):
                ans += n[i]
                ans += stack.pop()
        elif n[i] == '+' or n[i] == '-':
            stack.append(n[i])
        elif n[i] == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()  # ( 제거
while stack:
    ans += stack.pop()
print(ans)
