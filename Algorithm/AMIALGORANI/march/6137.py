"""
문자열 앞에걸 떼던가 뒤에걸 떼던가는 상관없음.
"""
from collections import deque

n = int(input())
s = deque([])
for _ in range(n):
    s.append(input())
answer = ""
cnt = 0
while s:
    if s[0] < s[-1]:
        answer += s.popleft()
    elif s[0] > s[-1]:
        answer += s.pop()
    else:
        left = 1
        right = len(s) - 2
        flag = False
        while left <= right:
            if s[left] < s[right]:
                answer += s.popleft()
                flag = True
                break
            elif s[left] > s[right]:
                answer += s.pop()
                flag = True
                break
            else:
                left += 1
                right -= 1
        if not flag:
            answer += s.pop()
    cnt += 1
    if cnt % 80 == 0:
        answer += '\n'
print(answer)
