import math

n = int(input())
stars = []
edges = []
for i in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))


def distance(a, b):
    return math.sqrt((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)


for i in range(n):
    for j in range(i + 1, n):
        dist = distance(stars[i], stars[j])
        edges.append((i, j, dist))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]


def get_parent(x):
    if x == parent[x]:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
for a, b, cost in edges:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        ans += cost
print(round(ans, 2))
