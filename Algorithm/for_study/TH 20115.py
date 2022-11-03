from itertools import combinations
n= int(input())
drink = list(map(int,input().split()))
drink.sort(reverse=True)
sum=0
# print(drink)
sum+=drink[0]
for i in range(1,n):
    sum+=drink[i]/2
if sum-int(sum)==0:
    print(int(sum))
else:
    print(sum)
