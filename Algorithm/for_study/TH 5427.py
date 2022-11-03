t=int(input())
def changegraph(graph,h,w):
    for i in range(h):
        for j in range(w):
            if graph[i][j]=='.':
                graph[i][j]=0 #빈공간
            elif graph[i][j]=='#':
                graph[i][j]=-1 #벽
            elif graph[i][j]=='@':
                graph[i][j]=7 # 상근이 위치
            elif graph[i][j]=='*':
                graph[i][j]=2 # 불 위치
    return graph

for _ in range(t):
    w,h = map(int,input().split())
    graph=[]
    for i in range(h):
        graph.append(list(input()))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    fireposition =



