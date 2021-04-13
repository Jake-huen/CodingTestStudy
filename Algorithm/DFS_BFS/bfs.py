from collections import deque

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5]
]
visited=[False]*9

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True