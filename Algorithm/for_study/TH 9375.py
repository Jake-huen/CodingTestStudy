# 안경, 코트, 상의, 신발
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    kind=dict()
    for i in range(n): #의상이름 의상종류
        a,b=input().split()
        if b in kind:
            kind[b].append(a)
        else:
            kind[b]=[a]
    temp=1
    #print(kind)
    for i in kind:
        temp=temp*(len(kind[i])+1)
    temp-=1
    ans.append(temp)
for i in range(len(ans)):
    print(ans[i])
