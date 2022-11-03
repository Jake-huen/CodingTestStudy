# 초고속 걷기 기계
n=int(input())
v=list(map(int,input().split()))
# (i-1)에서 i로 이동하는 데 필요한 속도
ans=0
for i in range(n-1,-1,-1):
    if ans<=v[i]:
        ans=v[i]
    else:
        if ans%v[i]:
            ans=(ans//v[i]+1)*v[i]
print(ans)