from collections import deque

n = int(input())
q = deque([(0, n)])
temp = ['A'] * n
ans = set()
while q:
    for _ in range(len(q)):
        start, end = q.popleft()
        if end - start <= 1:
            continue
        mid = (start + end) // 2
        for i in range(start, mid):
            temp[i] = 'A'
        for i in range(mid, end):
            temp[i] = 'B'
        q.append((start, mid))
        q.append((mid, end))
    ans.add(''.join(temp))
for a in ans:
    print(a)
for _ in range(7 - len(ans)):
    print('A' + ('B' * (n - 1)))
