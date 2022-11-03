import sys
input = sys.stdin.readline
n = int(input())
a,b = map(int,input().split())
graph=[]
for i in range(n):
    x,y = map(int,input().split())
    graph.append([x,y])
ans=0
graph.sort()
def bs(graph,target):
    first = 0
    end = len(graph)-1
    while first<=end:
        mid = (first+end)//2
        if graph[mid]==target:
            return True
        elif graph[mid]>target:
            end=mid-1
        elif graph[mid]<target:
            first=mid+1
    return False
for i in range(n):
    x = graph[i][0]
    y = graph[i][1]
    first = [x+a,y]
    second = [x,y+b]
    third = [x+a,y+b]
    if bs(graph,first) and bs(graph,second) and bs(graph,third):
        ans+=1
print(ans)