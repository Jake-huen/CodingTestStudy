n = int(input())
d = []#입력받는 RGB거리 value의 값
check=[False]*3#전에 뭐가 들어갔는지 체크
r=[0]*(n)
g=[0]*(n)
b=[0]*(n)
for i in range(n):
    d.append(list(map(int, input().split())))
r[0]=d[0][0]
g[0]=d[0][1]
b[0]=d[0][2]
for i in range(1,n):
    r[i]=d[i][0]+min(g[i-1],b[i-1])
    g[i]=d[i][1]+min(r[i-1],b[i-1])
    b[i]=d[i][2]+min(r[i-1],g[i-1])
print(min(r[n-1],g[n-1],b[n-1]))


