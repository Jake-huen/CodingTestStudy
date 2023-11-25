MIN = -1e9


class Node:
    def __init__(self, idx, time):
        self.idx = idx
        self.time = time


N = int(input())
road = list(map(int, input().split()))
cache = [Node(-1, -1) for _ in range(N)]
turn_point = [-1] * N


def go(idx):
    cache[idx] = Node(idx, 0)

    prev_pos = idx
    pos = idx + road[idx]
    time = 1
    while pos < N:
        if cache[pos].idx != -1:
            cache[idx] = Node(cache[pos].idx, cache[pos].time + time)
            break

        if road[pos] == 0:
            break

        prev_pos = pos
        pos += road[pos]
        time += 1

    if pos == N - 1:
        cache[idx] = Node(pos, time)
    elif pos >= N:
        cache[idx] = Node(prev_pos, time - 1)


def back(idx):
    if turn_point[idx] != -1:
        return turn_point[idx]

    turn_point[idx] = MIN

    if cache[idx].idx == N - 1:
        turn_point[idx] = cache[idx].time

    prev = idx - road[idx]
    if 0 <= prev:
        tmp = back(prev)
        turn_point[idx] = max(turn_point[idx], tmp + 1)

    return turn_point[idx]


for idx in range(N - 1, -1, -1):
    if road[idx] != 0:
        go(idx)

for idx in range(N - 1):
    if road[idx] != 0:
        back(idx)

pos, time = 0, 0
answer = -1
while pos < N:
    if road[pos] == 0:
        break

    answer = max(answer, time + turn_point[pos])
    pos += road[pos]
    time += 1

print(answer)
