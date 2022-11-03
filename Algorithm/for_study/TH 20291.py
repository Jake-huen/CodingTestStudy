n = int(input())
ans=[]
for i in range(n):
    temp = input()
    for i in range(len(temp)):
        if temp[i]=='.':
            ans.append(temp[i+1:])
ans.sort()
f = dict()
for i in range(len(ans)):
    if ans[i] in f:
        f[ans[i]]+=1
    else:
        f[ans[i]]=1
# print(f)
for yoso in f:
    print(yoso, f[yoso])
