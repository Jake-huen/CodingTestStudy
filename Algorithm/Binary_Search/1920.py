n = int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))

def binary_search(list,target,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if(list[mid]==target):
        return 1
    elif(list[mid]<target):
        start=mid+1
    elif(list[mid]>target):
        end=mid-1
    return binary_search(list,target,start,end)

for tar in b:
    result = binary_search(a,tar,0,len(a)-1)
    print(result)