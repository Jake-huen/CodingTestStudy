n = int(input())
a=list(map(int,input().split()))
#print(a)
d=[0]*(n)
d[0]=1
for i in range(1,n):
    for j in range(0,i):
        if a[i]<a[j]:
            d[i]=max(d[i],d[j])
    d[i]+=1
print(max(d))