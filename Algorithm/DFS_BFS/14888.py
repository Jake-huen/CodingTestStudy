from itertools import permutations
n = int(input())
a=list(map(int,input().split()))
operator=list(map(int,input().split()))
# operator조합으로 하면...?
op = list(permutations(operator,len(operator)))
print(op)
