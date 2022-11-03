# 길이 N짜리 수열 A
# A를 비내림차순으로 정렬, -> 수열 B
import sys
input = sys.stdin.readline
n,q = map(int,input().split())
a = list(map(int,input().split()))
a=sorted(a)
# print(a)
for i in range(1,n):
    a[i]=a[i]+a[i-1]
for i in range(q):
    l,r = map(int,input().split())
    if l==1:
        print(a[r-1])
    else:
        print(a[r-1]-a[l-2])