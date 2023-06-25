n, r, c = map(int, input().split())


def find(x, y, n):
    if x < 2 ** (n - 1) and y < 2 ** (n - 1):  # 1사분면
        return 1
    elif x < 2 ** (n - 1) <= y:
        return 2
    elif x >= 2 ** (n - 1) > y:
        return 3
    else:
        return 4


cnt = n
x = r   # 행
y = c   # 열
answer = []
while True:
    w = find(x, y, cnt)
    answer.append(w)
    if w == 2:
        y = y - 2 ** (cnt - 1)
    elif w == 3:
        x = x - 2 ** (cnt - 1)
    elif w == 4:
        x = x - 2 ** (cnt - 1)
        y = y - 2 ** (cnt - 1)
    cnt -= 1
    if cnt <= 1:
        answer.append(find(x, y, cnt))
        break
cnt = n
ans = 0
for w in answer:
    if w == 1:
        cnt -= 1
    elif w == 2:
        ans += 4 ** (cnt - 1)
        cnt -= 1
    elif w == 3:
        ans += 4 ** (cnt - 1) * 2
        cnt -= 1
    elif w == 4:
        ans += 4 ** (cnt - 1) * 3
        cnt -= 1
print(ans)
