import math
n = int(input())

for i in range(n):
    data = int(input())
    for d in data:
        prime = 0
        if d==1:
            continue
        for j in range(2,d+1):
            if d%j==0:
                prime = prime+1
        if prime=1:



