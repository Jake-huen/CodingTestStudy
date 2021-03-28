#https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2

import sys
sys.stdin.readline
n = int(input())
a=list(map(int,input().split()))
d=[0]
for i in range(n):
    start =0
    end=len(d)-1
    while start<=end:
        mid=(start+end)//2
        if d[mid]<a[i]:
            start=mid+1
        else:
            end=mid-1
    if start>=len(d):
        d.append(a[i])
    else:
        d[start]=a[i]
print(len(d)-1)