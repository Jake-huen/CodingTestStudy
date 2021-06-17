n=int(input())
a=list(map(int,input().split()))
dd=max(a)
flag=[True]*(dd+1)
flag[1]=False
temp=int(dd**0.5)
for i in range(2,temp+1):
    if flag[i]:
        for j in range(i+i,dd+1,i):
            flag[j]=False
number=0
for i in range(len(a)):
    if flag[a[i]]:
        number+=1
print(number)