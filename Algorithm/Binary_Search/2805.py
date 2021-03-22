import sys
sys.stdin.readline

n,m = map(int,input().split())
tree=list(map(int,input().split()))

start = 1
end = max(tree)
ans=0

while start<=end:
    mid=(start+end)//2
    result=0
    for i in tree:
        if mid<i:
            result+=i-mid
    if result>=m:
        ans=mid
        start=mid+1
    elif result<m:
        end=mid-1
print(ans)

