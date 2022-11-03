n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split().append(1))))
print(graph)
def check(x,y,n):
    temp = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if temp!=graph[i][j]:
                print('(',end='')
                check(x,y,n//2)
                check(x,y+n//2,)
    if check==-1:

