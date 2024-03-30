"""
1부터 N까지의 수 이어쓰면 1234567891011...
k번째 자리 숫자가 어떤 숫자인지 구하는 프로그램
"""

n, k = map(int, input().split())
total_length = 0
digit = len(str(n))
digit_arr = []

for i in range(1, digit + 1):
    temp = int(i * (10 ** i - 10 ** (i - 1)))
    digit_arr.append(temp)
    if i < digit:
        total_length += temp

total_length += (n - 10 ** (digit - 1) + 1)
if k > total_length:
    print(-1)
else:
    