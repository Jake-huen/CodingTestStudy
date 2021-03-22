n = int(input())

s=0

a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(n):
    s+=a[i]*b[i]

print(s)

#://shoark7.github.io/programming/algorithm/second-largest-number-in-array