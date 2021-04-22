n = int(input())
num=list(map(int,input().split()))
d=[0]*10000
d[0]=num[0]
for i in range(1,n):
    d[i]=max(d[i-1]+num[i],num[i])
print(d[n-1])