# 장미 n개 선물
n,a,b,c,d = list(map(int,input().split()))
ans=0
buy=0
more_buy=0
if (n//a)*b<(n//c)*d:
    buy=n//a*a
    more_buy = n%a
    ans+=(n//a)*b
else:
    buy=n//c*c
    more_buy=n%c
    ans+=(n//c)*d
print(ans)
