"""
n개의 세로선
m개의 가로선
각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 h
i번의 세로선의 결과가 i번이 나와야 함.
추가해야 하는 가로선 개수의 최솟값을 구해라.

먼저 조건대로 나두었을 때 어떻게 가는지 알고, 하나씩 추가해서 결과를 비교하면 될듯
"""
n, m, h = map(int, input().split())
garo = [[False for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())  # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
    garo[a - 1][b - 1] = True  # a-1번째 줄에 b-1과 b 연결되어 있음


def sadari_result():
    for i in range(n):
        temp = i
        for j in range(h):
            if garo[j][temp]:
                temp = temp + 1
            elif garo[j][temp - 1]:
                temp = temp - 1
        if i != temp:
            return False
    return True


ans = 4


def dfs(cnt, x, y): # 횟수, 행, 열
    global ans
    if sadari_result():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x, h):  # 행
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n - 1):
            if not garo[i][j] and not garo[i][j + 1]:
                if j > 0 and garo[i][j - 1]:
                    continue
                garo[i][j] = True
                dfs(cnt + 1, i, j + 2)
                garo[i][j] = False


dfs(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)
