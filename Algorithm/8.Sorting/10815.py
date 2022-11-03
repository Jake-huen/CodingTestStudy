import sys
sys.stdin.readline
#binary_search 사용
n= int(input())
data = list(map(int,input().split()))
m=int(input())
checks=list(map(int,input().split()))
data.sort()
def binary_search(target,start,end):
    while start<=end:
        mid = (start+end)//2
        if data[mid] == target:
            print(1,end=' ')
            return
        elif data[mid]<target:
            start=mid+1
        elif data[mid]>target:
            end=mid-1
    print(0,end=' ')
for check in checks:
    start =0
    end = len(data)-1
    binary_search(check,start,end)
#in은 리스트 전체를 순회하기 때문에 시간초과가 난다.
# for check in checks:
#     if check in data:
#         print(1,end=' ')
#     else: print(0,end=' ')