import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b)
    elif op == 1:
        if a == b:
            print("YES")
        elif find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
