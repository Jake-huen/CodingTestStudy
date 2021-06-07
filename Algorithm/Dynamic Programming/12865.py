n,k = map(int,input().split())
things=[[0]*2 for _ in range(n)]
d=[0]*(k+1)
for i in range(n):
    w,v=map(int,input().split())
    things[i][0]=w
    things[i][1]=v
    d[w]=v
#print(things)
#print(d)
for i in range(1,k+1):
    for j in range(n):
        temp=things[j][0]
        if i-temp>=0:
            d[i]=max(d[i],d[i-temp]+things[j][1])
print(d[k])