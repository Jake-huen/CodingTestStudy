n = int(input()) # 굴다리 길이
m = int(input()) # 가로등 개수
x = list(map(int,input().split()))
ans=0
if len(x)==1:
    ans=max(x[0],n-x[0])
else:
    for i in range(len(x)):
        if i==0:
            h=x[0]
        elif i==len(x)-1:
            h = n-x[i]
        else:
            temp = x[i]-x[i-1]
            if temp%2==0:
                h = temp//2+1
            else:
                h = temp//2
        ans = max(ans,h)
print(ans)
