k = int(input())
visited = list(map(int,input().split()))
temp = len(visited)
answer = [[] for _ in range(k)]
def tree(x, visited,start,end):
    if x>=k:
        return
    mid = (end-start)//2+start
    answer[x].append(visited[mid])
    x+=1
    tree(x,visited,start,mid-1)
    tree(x,visited,mid+1,end)
    return
tree(0,visited,0,temp)
for i in range(k):
    for j in range(len(answer[i])):
        print(answer[i][j],end=' ')
    print()
