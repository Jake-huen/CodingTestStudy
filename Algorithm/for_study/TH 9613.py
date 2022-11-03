import math
t= int(input())

for i in range(t):
    tc = list(map(int,input().split()))
    total=0
    for j in range(1,len(tc)):
        for k in range(j+1,len(tc)):
            total+=math.gcd(tc[j],tc[k])
    print(total)