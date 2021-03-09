n = int(input())

d = [10001]*5001
d[0]=0
for i in range(3,n+1):
    if i-5>=0 and d[i-5]!=10001:
        d[i]=min(d[i],d[i-5]+1)
    if d[i-3]!=10001:
        d[i]=min(d[i],d[i-3]+1)

if d[n]==10001:
    print(-1)
else:
    print(d[n])
