n = int(input())
sul=[]
d=[0]*10000
for i in range(n):
    sul.append(int(input()))
d[0]=sul[0]
if n>1:
    d[1]=sul[0]+sul[1]
if n>2:
    d[2]=max(sul[0]+sul[2],sul[1]+sul[2],d[1])

for i in range(3,n):
    d[i]=max(d[i-2]+sul[i],d[i-3]+sul[i-1]+sul[i],d[i-1])

print(d[n-1])