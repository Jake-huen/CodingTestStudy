import sys
sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
m = int(input())
data.sort()
start=0
end=data[-1]
ans=0
while start<=end:
    mid=(start+end)//2
    total=0
    for i in data:
        if i<=mid:
            total+=i
        elif i>mid:
            total+=mid
    if total>m:
        end=mid-1
    elif total<=m:
        ans=mid
        start=mid+1
print(ans)
