from collections import deque

n, k = map(int, input().split())

answer = 0

visited = set()
visited.add((n, 0))
q = deque()
q.append([n, 0])

while q:
    cur, cnt = q.popleft()
    if cnt == k:
        answer = max(answer, cur)
    else:
        temp = list(str(cur))
        for i in range(len(str(n)) - 1):
            for j in range(i + 1, len(str(n))):
                if i == 0 and temp[j] == '0':
                    continue
                temp[i], temp[j] = temp[j], temp[i]
                num = int(''.join(temp))
                if (num, cnt + 1) not in visited:
                    visited.add((num, cnt + 1))
                    q.append([num, cnt + 1])
                temp[i], temp[j] = temp[j], temp[i]
if answer == 0:
    print(-1)
else:
    print(answer)
