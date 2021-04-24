n = int(input())
num=list(map(int,input().split()))
m=[0]*100000
ans=-999999
m[0]=num[0]
for i in range(n):
    m[i]=max(m[i-1]+num[i],num[i])
    ans=max(ans,m[i])
print(ans)