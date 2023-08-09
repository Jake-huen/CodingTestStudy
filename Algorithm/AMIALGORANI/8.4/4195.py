



def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        counter[a] += counter[b]

t = int(input())
for _ in range(t):
    parents = {}
    counter = {}
    f = int(input())  # 친구 관계의 수
    for _ in range(f):
        a, b = input().split()
        if a not in parents:
            parents[a] = a
            counter[a] = 1
        if b not in parents:
            parents[b] = b
            counter[b] = 1
        union(a, b)
        print(counter[find(a)])
