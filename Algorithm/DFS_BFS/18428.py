from collections import deque
from itertools import combinations
n = int(input())
graph=[]
for i in range(n):
    graph.append(list(input().split()))
copy_graph=[[0]*(n) for _ in range(n)]
def copy():
    for i in range(n):
        for j in range(n):
            copy_graph[i][j]=graph[i][j]
def bfs():
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='T':
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(x+1,n):
            if copy_graph[i][y]=='X' or copy_graph[i][y]=='T':
                continue
            elif copy_graph[i][y]=='O':
                break
            elif copy_graph[i][y]=='S':
                return False
        for i in range(x-1,-1,-1):
            if copy_graph[i][y]=='X' or copy_graph[i][y]=='T':
                continue
            elif copy_graph[i][y]=='O':
                break
            elif copy_graph[i][y]=='S':
                return False
        for i in range(y+1,n):
            if copy_graph[x][i]=='X':
                continue
            elif copy_graph[x][i]=='O':
                break
            elif copy_graph[x][i]=='S':
                return False
        for i in range(y-1,0,-1):
            if copy_graph[x][i]=='X':
                continue
            elif copy_graph[x][i]=='O':
                break
            elif copy_graph[x][i]=='S':
                return False
    return True
def obs():
    q=deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='X':
                q.append((i,j))
    a = list(combinations(q, 3))
    for i in range(len(a)):
        copy()
        for j in range(3):
            x=a[i][j][0]
            y=a[i][j][1]
            copy_graph[x][y]='O'
        if bfs():
            return 'YES'
    return 'NO'

print(obs())