#숫자카드 2
import sys
sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
m = int(input())
checks = list(map(int,input().split()))
def binary_search(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            print
        elif data[mid]<target:
            start = mid+1
        elif data[mid]>target:
            end = mid-1
for check in checks:
    start=0
    end = n-1
    binary_search(check,start,end)
