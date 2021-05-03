n=int(input())
for _ in range(n):
    s = input()
    result=0
    suc=0
    for i in range(len(s)):
        if s[i]=='O':
            if i-1==-1 or s[i-1]=='X':
                suc=1
            elif s[i-1]=='O':
                suc+=1
            result+=suc
    print(result)