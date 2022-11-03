n,k=map(int,input().split())
ondo = list(map(int,input().split()))
ans=-999999999
temp=0
for i in range(k):
    temp+=ondo[i]
ans=max(temp,ans)
for i in range(1,n-k+1):
    temp=temp-ondo[i-1]+ondo[i+k-1]
    if temp>ans:
        ans=temp
print(ans)
