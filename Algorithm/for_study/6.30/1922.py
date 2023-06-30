n = int(input())
m = int(input())
graph = []

parent = [i for i in range(n + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
graph.sort(key=lambda x: x[2])
ans = 0
for a, b, cost in graph:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        ans += cost
print(ans)
