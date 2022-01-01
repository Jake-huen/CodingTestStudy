import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
answer=0

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

def dijkstra(start,end):
    q=[]
    distance = [INF] * (n + 1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]
path1 = dijkstra(1,v1) + dijkstra(v1,v2)+dijkstra(v2,n)
path2 = dijkstra(1,v2) + dijkstra(v2,v1)+dijkstra(v1,n)
answer = min(path1,path2)
if answer>=INF:
    print(-1)
else:
    print(answer)







#플로이드 워셜 -> 시간 초과 남
# graph=[[INF]*(n+1) for _ in range(n+1)]
# for i in range(e):
#     a,b,c = map(int,input().split())
#     graph[a][b]=c
#     graph[b][a]=c
# v1,v2 = map(int,input().split())
# # print(graph)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         for k in range(1,n+1):
#             if graph[i][j]>graph[i][k]+graph[k][j]:
#                 graph[i][j]=graph[i][k]+graph[k][j]
# answer=min(graph[1][v1]+graph[v1][v2]+graph[v2][n],graph[1][v2]+graph[v2][v1]+graph[v1][n])
# print(answer)
