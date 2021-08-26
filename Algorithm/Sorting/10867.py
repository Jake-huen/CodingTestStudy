n=int(input())
l=set(map(int,input().split()))
l=list(l)
l.sort()
for i in range(len(l)):
    print(l[i],end=' ')