import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stocks=list(map(int,input().split()))
    result =0
    big=0
    for i in range(n-1,-1,-1):
        if stocks[i]>big:
            big=stocks[i]
        if big-stocks[i]>0:
            result+=big-stocks[i]
    print(result)
