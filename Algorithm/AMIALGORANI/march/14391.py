"""
자를때 가로가 1 or 세로가 1
가로는 1이 있는 수, 세로는 0이 있는 수 이런식으로 하기
"""

n, m = map(int, input().split())  # 가로 m, 세로 n

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)

# for i in range(pow(2, n * m)):
    