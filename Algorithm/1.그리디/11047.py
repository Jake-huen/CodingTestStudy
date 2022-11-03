n,k=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
ans=0
for i in range(n):
    if a[i]>k:
        continue
    else:
        ans+=k//a[i]
        k=k%a[i]
print(ans)