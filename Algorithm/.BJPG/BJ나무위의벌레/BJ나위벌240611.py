"""
임의의 한점에서 가장 먼 점 A를 구하고, 해당 점에서 가장 먼 점 B를 연결하는 AB가 가장 긴 길이

주의 : 길이가 같은 지름이 여러개 존재할 수 있으므로, 길이가 같은 것을 다 구해서 모두 구해줘야 한다. 
"""

import sys
from collections import deque

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def DFS(n):
    distances = [-1] * (n + 1)  # n부터 각 노드까지의 열매점수
    q = deque([[n, n]])
    distances[n] = [fruits[n - 1], [n, n]]

    maxDis = 0
    nodeList = []
    while q:
        route = q.pop()
        now = route[0] # 현재 열매 정도

        for next in graph[now]:
            if distances[next] == -1:
                temp = route[:]
                temp[0] = next
                dis = distances[now][0] + fruits[next - 1]
                distances[next] = [dis, temp]
                q.append(temp)
                if maxDis < dis:
                    maxDis = dis
                    nodeList = [next]
                elif maxDis == dis:
                    nodeList.append(next)
    same = {}
    for node in nodeList:
        same[node] = [distances[node][0], min(distances[node][1])]
    return same


dis = DFS(1)
maxDis = -1
ansNode = -1
for node in dis:
    finalDis = DFS(node)
    for ans in finalDis:
        if maxDis < finalDis[ans][0]:
            maxDis = finalDis[ans][0]
            ansNode = finalDis[ans][1]
        if maxDis == finalDis[ans][0]:
            ansNode = min(finalDis[ans][1], ansNode)
if n == 1:
    print(fruits[0], 1)
else:
    print(maxDis, ansNode)
