n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
"""
길의 개수는 2n개
길을 지나갈 수 있으려면 칸의 높이가 모두 같거나, 경사로로 지나갈 수 있는 길을 만들 수 있어야 함. 
경사로 : 낮은 칸과 높은 칸 연결 -> 차이 : 1
높이가 같은 L개의 연속된 칸(같은 높이) 
"""


def check(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:  # 1차이나는 경우
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or visited[i + j]:
                    return False
                if line[i] == line[i + j]:
                    visited[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or visited[i - j - 1]:
                    return False
                if line[i - j - 1] == line[i - 1]:
                    visited[i - j - 1] = True
    return True

ans = 0
for i in range(n):
    visited = [False] * n
    if check([graph[i][j] for j in range(n)]):
        ans += 1
for j in range(n):
    visited = [False] * n
    if check([graph[i][j] for i in range(n)]):
        ans += 1
print(ans)
