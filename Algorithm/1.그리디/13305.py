n = int(input())
dist=list(map(int,input().split()))
gireum=list(map(int,input().split()))
result=gireum[0]*dist[0]
first=gireum[0]
for i in range(1,len(gireum)-1):
    if gireum[i]<first:
        result+=gireum[i]*dist[i]
        first=gireum[i]
    else:
        result+=first*dist[i]
print(result)