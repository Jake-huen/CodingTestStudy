from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start):
    q = deque()
    q.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while q:
        x = q.popleft()
        color = visited[x]
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == color:
                return False
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    flag =0
    for i in range(1, v + 1):
        if not bfs(graph, i):
            flag = 1
            print("NO")
            break
    if flag==0:
        print("YES")
