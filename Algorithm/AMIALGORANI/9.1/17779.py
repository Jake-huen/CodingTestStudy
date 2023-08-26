n = int(input())
graph = [] * (n)
for i in range(n):
    graph.append(list(map(int, input().split())))
# 일단 경우를 다 해봐야 할 것 같음.
# x는 1부터 N-1까지 가능
boundaries = []
for n in range(5, 21):  # n의 범위
    for x in range(1, n - 2):  # x의 범위
        for y in range(1, n):  # y의 범위
            for d1 in range(1, y):  # d1의 범위
                for d2 in range(1, n - y + 1):  # d2의 범위
                    if x + d1 + d2 <= n:
                        boundaries.append((n, x, y, d1, d2))
for boundary in boundaries:
    b_n, x, y, d1, d2 = boundary
    one, two, three, four, five = 0, 0, 0, 0, 0
    for r in range(1, b_n + 1):
        r1 = r - 1
        for c in range(1, b_n + 1):
            c1 = c - 1
            if 1 <= r < x + d1 and 1 <= c <= y:
                one += graph[r1][c1]
            elif 1 <= r <= x + d2 and y < c <= b_n:
                two += graph[r1][c1]
            elif x + d1 <= r <= b_n and 1 <= c < y - d1 + d2:
                three += graph[r1][c1]
            elif x + d2 < r <= b_n and y - d1 + d2 <= c <= b_n:
                four += graph[r1][c1]
            else:
                five += graph[r1][c1]
    # print(one, two, three, four, five)
