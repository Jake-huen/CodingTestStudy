#N+1 일째 되는 날 퇴사 N일동안 상담.
n = int(input())
t=[]
p=[]
d=[0]*(n+1)
for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)
for i in range(n-1,-1,-1):
    if i+t[i]>n:
        d[i]=d[i+1]
    else:
        d[i]=max(p[i]+d[i+t[i]],d[i+1])
print(d[0])