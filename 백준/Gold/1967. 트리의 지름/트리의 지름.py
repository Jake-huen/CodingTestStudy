'''
2초 -> 2억
n = 10 4
n 제곱까지 가능
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
leaf_graph = [[] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    p, c, w = map(int, input().split())
    leaf_graph[p].append([c, w])
    graph[p].append([c, w])
    graph[c].append([p, w])


# leaf 노드 체크
def check_leaf():
    visited = [False for _ in range(n + 1)]
    q = deque()
    q.append(1)
    answer = []
    while q:
        start = q.pop()
        if len(leaf_graph[start]) == 0:
            answer.append(start)
        for nn in leaf_graph[start]:
            next_node = nn[0]
            if not visited[next_node]:
                q.append(next_node)
    return answer


# leaf_node 각각 bfs
leaf_node = check_leaf()


def bfs(start, n):
    q = deque()
    q.append(ln)
    visited = [False for _ in range(n + 1)]
    node_weight = [0 for _ in range(n + 1)]
    while q:
        start = q.pop()
        visited[start] = True
        for n in graph[start]:
            if not visited[n[0]]:
                node_weight[n[0]] = node_weight[start] + n[1]
                visited[n[0]] = True
                q.append(n[0])
    return max(node_weight)


ans = []
for ln in leaf_node:
    ans.append(bfs(ln, n))
print(max(ans))
