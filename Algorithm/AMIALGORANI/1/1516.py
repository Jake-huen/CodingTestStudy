"""
자원은 무한히 많이 가짐, 건물을 짓는 명령을 내리기까지는 시간이 걸리지 않음.
"""
from collections import deque

n = int(input())
buildings = [[] for _ in range(n + 1)]
node_in = [0] * (n + 1)
time = [0] * (n + 1)
for building_number in range(1, n + 1):
    temp_input = list(map(int, input().split()))
    time[building_number] = temp_input[0]
    build_data = temp_input[1:-1]
    for i in build_data:
        buildings[i].append(building_number)
        node_in[building_number] += 1
# print(buildings)
# print(node_in)
# print(time)
q = deque()
for i in range(1, n + 1):
    if node_in[i] == 0:
        q.append(i)
# print(q)
answer = [0] * (n + 1)
while q:
    cur = q.popleft()
    answer[cur] += time[cur]  # 일단 얘가 지어질동안 나머지 애들도 다 기다려야함.
    for b in buildings[cur]:
        node_in[b] -= 1
        answer[b] = max(answer[b], answer[cur])
        if node_in[b] == 0:
            q.append(b)
for i in range(1, len(answer)):
    print(answer[i])
