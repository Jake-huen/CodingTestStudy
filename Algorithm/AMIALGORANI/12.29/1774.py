n, m = map(int, input().split())
god = []
for _ in range(n):
    x, y = map(int, input().split())
    god.append([x, y])


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x,y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    parent[max]


"""우주신과의 교감
매번 여러 우주신과 교감해야함

"""
