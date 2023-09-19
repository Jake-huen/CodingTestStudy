from collections import deque


def solution(n, m, x, y, r, c, k):
    # d, l, r, u 사전 순
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    x = x - 1
    y = y - 1
    r = r - 1
    c = c - 1
    q = deque()
    q.append([x, y, ""])  # 출발점 추가
    while q:
        node_r, node_c, ans = q.popleft()
        if len(ans) == k and node_r == r and node_c == c:
            return ans
        if len(ans) > k:
            break
        for i in range(4):
            nr = node_r + dr[i]
            nc = node_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if i == 0:
                    n_ans = ans + 'd'
                elif i == 1:
                    n_ans = ans + 'l'
                elif i == 2:
                    n_ans = ans + 'r'
                elif i == 3:
                    n_ans = ans + 'u'
                q.append([nr, nc, n_ans])
    return "impossible"


print(solution(3, 4, 2, 3, 3, 1, 5))
