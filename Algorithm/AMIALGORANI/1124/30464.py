import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
answer = []


def DFS(cur, turn, count, dir):
    if turn > 2:
        return
    if cur == n - 1:
        answer.append(count)
        return
    if cur > n - 1:
        return
    if cur < 0:
        return
    else:
        if dir == 0:
            DFS(cur + a[cur], turn, count + 1, 0)
            DFS(cur - a[cur], turn + 1, count + 1, 1)
        elif dir == 1:
            DFS(cur - a[cur], turn, count + 1, 1)
            DFS(cur + a[cur], turn + 1, count + 1, 0)


DFS(0, 0, 0, 0)
if answer:
    print(max(answer))
else:
    print(-1)
