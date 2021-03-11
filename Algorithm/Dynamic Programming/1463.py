# 1로 만들기
import sys
input = sys.stdin.readline
n = int(input())

d = [0] * 100001

def make1(x):
    for i in range(2,x+1):
        d[i]=d[i-1]
        if i%3==0:
            d[i]=min(d[i],d[i//3])
        if i%2==0:
            d[i]=min(d[i],d[i//2])
        d[i]+=1
    return d[x]
print(make1(n))

# while n!=1:
#     if n%3==0:
#         result += 1
#         n=n/3
#     if n%2==0:
#         result += 1
#         n=n/2
#     else:
#         result += 1
#         n=n-1


#for i in range(2, n + 1):
#    d[i] = d[i - 1] + 1
#    if i % 3 == 0:
#        d[i] = min(d[i // 3] + 1, d[i])
#    if i % 2 == 0:
#        d[i] = min(d[i // 2] + 1, d[i])
#
#print(d[n])