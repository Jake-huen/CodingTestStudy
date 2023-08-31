from collections import deque

n = int(input())
hate = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    p = list(map(int, input().split()))
    hate[i] = p[1:]
q = deque()
blue = set()
white = set()
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        q.append([i, 'B'])
        blue.add(i)
        while q:
            x, team = q.popleft()
            hate_people = hate[x]
            if team == 'B':
                for p in hate_people:
                    if not visited[p]:
                        q.append((p, 'W'))
                        white.add(p)
                        visited[p] = True
            elif team == 'W':
                for p in hate_people:
                    if not visited[p]:
                        q.append((p, 'B'))
                        blue.add(p)
                        visited[p] = True
blue = list(blue)
white = list(white)
blue.sort()
white.sort()
if len(blue) == 0:
    blue = [i for i in range(1, n + 1)]
print(len(blue))
print(*blue)
print(len(white))
print(*white)

# 청팀 사람수
# 청팀 멤버
# 백팀 사람수
# 백팀 멤버
