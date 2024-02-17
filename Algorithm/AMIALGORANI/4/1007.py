from itertools import combinations
import math
t = int(input())
for _ in range(t):
    n = int(input())
    ans = int(1e9)
    graph = []
    total_x = 0
    total_y = 0
    for i in range(n):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        graph.append([x, y])
    combis = list(combinations(graph, n // 2))
    combis = combis[:(len(combis) // 2)]
    # print(combis)
    for combi in combis:
        first_x = 0
        first_y = 0
        for tmp in combi:
            first_x += tmp[0]
            first_y += tmp[1]
        second_x = total_x - first_x
        second_y = total_y - first_y
        # [first_x, first_y]
        # [second_x, second_y]
        temp = math.sqrt((second_x-first_x)**2 + (second_y - first_y)**2)
        ans = min(temp, ans)
    print(ans)


