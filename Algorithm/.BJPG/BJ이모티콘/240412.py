import sys
from collections import deque

INF = sys.maxsize
"""
1. 화면에 있는 이모티콘 모두 복사해서 클립보드에 저장
2. 클립보드에 있는 모든 이코티콘 화면에 붙여넣기
3. 화면에 있는 이모티콘 중 하나 삭제
모든 연산은 1초.
화면에 이모티콘 붙여넣기 하면 클립보드에 있는 이모티콘 개수가 화면에 추가
"""

s = int(input())
dp = [[-1 for _ in range(s+1)] for _ in range(s + 1)]
dp[1][0] = 0
q = deque()
q.append([1, 0])
while q:
    x, clip = q.popleft()
    if dp[x][x] == -1:
        dp[x][x] = dp[x][clip] + 1
        q.append((x, x))
    if x + clip <= s and dp[x + clip][clip] == -1:
        dp[x + clip][clip] = dp[x][clip] + 1
        q.append((x + clip, clip))
    if x - 1 >= 0 and dp[x - 1][clip] == -1:
        dp[x - 1][clip] = dp[x][clip] + 1
        q.append((x - 1, clip))

answer = INF
for i in range(s + 1):
    if dp[s][i] != -1:
        answer = min(answer, dp[s][i])
print(answer)
