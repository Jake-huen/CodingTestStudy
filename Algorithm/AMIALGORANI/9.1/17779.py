n = int(input())
graph = [[0] * (n + 1)]
for i in range(n):
    graph.append([0] + list(map(int, input().split())))
#print(graph)
ans = []
total = 0
for i in range(1, n + 1):
    total += sum(graph[i])
# 일단 경우를 다 해봐야 할 것 같음.
# x는 1부터 N-1까지 가능
boundaries = []
for x in range(1, n + 1):  # x의 범위
    for y in range(1, n + 1):  # y의 범위
        for d1 in range(1, n + 1):  # d1의 범위
            for d2 in range(1, n + 1):  # d2의 범위
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                boundaries.append((x, y, d1, d2))

for boundary in boundaries:
    x, y, d1, d2 = boundary
    count = [0] * 5
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    # 2번 조건
    temp[x][y] = 5
    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        temp[x + d2 + i][y + d2 - i] = 5

    count = [0] * 5
    # 1번 선거구
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if temp[r][c] == 5:
                break
            else:
                count[0] += graph[r][c]

    # 2번 선거구
    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            else:
                count[1] += graph[r][c]

    # 3번 선거구
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if temp[r][c] == 5:
                break
            else:
                count[2] += graph[r][c]

    # 4번 선거구
    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            else:
                count[3] += graph[r][c]

    # 5번 선거구
    count[4] = total - sum(count)
    ans.append(max(count) - min(count))
print(min(ans))
