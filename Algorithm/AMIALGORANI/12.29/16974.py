n, x = map(int, input().split())
bugger = [0] * 51
patty = [0] * 51
bugger[0] = 1
patty[0] = 1
for i in range(1, n + 1):
    bugger[i] = 1 + bugger[i - 1] + 1 + bugger[i - 1] + 1
    patty[i] = patty[i - 1] + 1 + patty[i - 1]


def eat(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + bugger[n - 1]:
        return eat(n - 1, x - 1)
    elif x == 1 + bugger[n - 1] + 1:
        return patty[n - 1] + 1
    elif x <= bugger[n - 1] + bugger[n - 1] + 1 + 1:
        return patty[n - 1] + 1 + eat(n - 1, (x - bugger[n - 1] - 2)) # 맨끝 버거 패티, 중간 패티 1개 무조건
    else:
        return patty[n]


print(eat(n, x))

""" 레벨 햄버거
B + (N-1)버거 + P + (N-1)버거 + B

x <= (N-1)버거 + 1
x == 1+ (N-1)버거 + 1
x <= 1+ (N-1)버거 + 1 + (N-1)버거
다 쳐먹은 경우
"""
