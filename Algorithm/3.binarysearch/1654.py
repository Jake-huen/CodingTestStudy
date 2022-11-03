import sys
sys.stdin.readline

k,n = map(int,input().split())
data=[]
for _ in range(k):
    data.append(int(input()))

start=1
end=max(data)
ans=0
while start<=end:
    mid=(start+end)//2
    result=0
    for i in data:
        if mid!=0:
            result+=i//mid
    if result<n:
        end=mid-1
    elif result>=n:
        ans=mid
        start=mid+1
print(ans)