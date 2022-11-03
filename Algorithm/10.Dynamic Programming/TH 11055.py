n = int(input())
a=list(map(int,input().split()))
#앞에 것들중 최대
#print(a)
d=[0]*(n)
d[0]=a[0]
for i in range(1,n):
    for j in range(0,i):
        if a[i]>a[j]:
            d[i]=max(d[i],d[j])
    d[i]+=a[i]
print(max(d))