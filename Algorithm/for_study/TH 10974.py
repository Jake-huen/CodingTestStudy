import itertools
n=int(input())
arr=[i+1 for i in range(n)]
npr=list(itertools.permutations(arr,n))
for i in range(len(npr)):
    print(*npr[i])