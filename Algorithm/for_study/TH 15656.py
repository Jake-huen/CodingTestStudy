import itertools
n,m = map(int,input().split())
temp=sorted(list(map(int,input().split())))
npr=list(itertools.product(temp,repeat=m))
# print(*npr)
for i in range(len(npr)):
    print(*npr[i])
