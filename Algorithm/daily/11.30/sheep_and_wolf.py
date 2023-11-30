from collections import deque


def solution(info, edges):
    answer = 0
    tree = {i: [] for i in range(len(info))}
    for p, c in edges:
        tree[p].append(c)
    q = deque([])
    q.append([0, tree[0], 1, 0])  # now, can_move, sheep, wolf
    while q:
        now, can_move, sheep, wolf = q.popleft()
        if sheep > answer:
            answer = sheep
        for i, node in enumerate(can_move):
            if info[node] == 0:  # 양인 경우
                q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep + 1, wolf])
            elif info[node] == 1:
                if sheep > wolf + 1:
                    q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep, wolf + 1])
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
