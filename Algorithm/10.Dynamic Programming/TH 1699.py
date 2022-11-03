import math
import sys
n = int(sys.stdin.readline().rstrip())
d=[9999]*(n+1)
for i in range(1,n+1):
    if math.sqrt(i)-int(math.sqrt(i))==0:
        d[i]=1
    else:
        for j in range(1,i):
            if d[j]==1:
                d[i]=min(d[j]+d[i-j],d[i])
print(d[n])