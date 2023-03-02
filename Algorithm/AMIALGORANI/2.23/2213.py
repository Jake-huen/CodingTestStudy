# from itertools import combinations
#
# n = int(input())
# w = list(map(int, input().split()))
# graph = [[0] for _ in range(n + 1)]
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
#
# def check_is(nodes):
#     for node in nodes:
#         for idx in nodes:
#             if idx in graph[node]:
#                 return False
#     return True
#
#
# def weight(nodes):
#     ans = 0
#     for node in nodes:
#         ans += w[node - 1]
#     return ans
#
#
# answers = []
# for i in range(1, n + 1):
#     temp = [lk for lk in range(1, n + 1)]
#     cases = list(combinations(temp, i))
#     for case in cases:
#         if check_is(case):
#             answers.append((weight(case), case))
# print(max(answers)[0])
# print(*max(answers)[1])

import sys
input = sys.stdin.readline
n = int(input())
weight = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
DP = [[0, 0] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]


def dfs(cur):
    visited[cur] = True  # 방문체크
    DP[cur][0] = weight[cur]  # 현재 노드 포함할때
    DP[cur][1] = 0  # 현재 노드 포함하지 않을때
    for i in graph[cur]:  # 연결된 노드 탐색
        if not visited[i]:
            dfs(i)
            DP[cur][0] += DP[i][1]  # 해당노드 포함했을때
            DP[cur][1] += max(DP[i][0], DP[i][1])  # 해당노드 포함 안했을때


trace_result = []
trace_check = [False for _ in range(n + 1)]


def trace(cur, pre):  # 현재노드와 이전노드가 포함되었는지 안되었는지 0:포함됨 1:포함안됨
    trace_check[cur] = True

    if pre == 0:  # 이전노드가 포함되었다면
        for i in graph[cur]:  # 현재노드는 포함할수없음
            if not trace_check[i]:
                trace(i, 1)
    else:  # 이전노드가 포함되어있지않다면
        if DP[cur][0] > DP[cur][1]:  # 현재노드를 포함한 부분이 더크다면
            trace_result.append(cur)  # 현재노드 포함
            for i in graph[cur]:
                if not trace_check[i]:
                    trace(i, 0)
        else:  # 현재노드를 포함하지 않은부분이 크다면
            for i in graph[cur]:
                if not trace_check[i]:
                    trace(i, 1)


dfs(1)
print(max(DP[1][0], DP[1][1]))
trace(1, 1)  # 임의의 루트노드지정 ,이전노드가 없으므로 1로 둔다
trace_result.sort()  # 오름차순정렬
print(*trace_result)
