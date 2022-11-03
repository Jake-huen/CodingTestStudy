n = int(input())
p = list(map(int,input().split()))
p.insert(0,0)
d = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i):
        d[i] = max(d[i],p[i-j]+d[j])
print(d[n])