n=int(input())
a=list(map(int,input().split()))
m=int(input())
answer=[]
d=[0]*(n+1)
d[1]=a[0]
for i in range(2,n+1):
    d[i]=d[i-1]+a[i-1]
for i in range(m):
    x,y=map(int,input().split())
    temp=0
    temp=d[y]-d[x-1]
    answer.append(temp)
for i in answer:
    print(i)