from collections import deque
import sys

input = sys.stdin.readline


def trace(k):
    if k == 0:
        return
    trace(visited[k])
    print(k - visited[k], end=" ")


n = int(input())
gms = []

for i in range(2, 300):
    nums = []
    temp = i
    while temp:
        nums.append(temp % 2)
        temp = temp // 2
    ans = ""
    for j in range(len(nums) - 2, -1, -1):
        if nums[j] == 0:
            ans += "4"
        elif nums[j] == 1:
            ans += "7"
    gms.append(int(ans))

visited = [-1] * 1000000001
q = deque()
q.append(0)

while q:
    cur = q.popleft()
    if cur == n:
        break
    for i in range(len(gms)):
        next = cur + gms[i]
        if next > n:
            break
        if visited[next] == -1:
            visited[next] = cur
            q.append(next)

if visited[n] == -1:
    print(-1)
else:
    trace(n)
# 898989
# 4 4744 4747 444747 444747
