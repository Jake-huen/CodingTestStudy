# I, V, X,  L
# 1, 5, 10, 50
# XXXV : 35 IXI : 12
import itertools
n = int(input())
numbers=[1,5,10,50]
ans=[]
ways = list(itertools.combinations_with_replacement(numbers,n))
# print(way[0])
for way in ways:
    sum=0
    for j in range(n):
        sum+=way[j]
    ans.append(sum)
print(len(set(ans)))
