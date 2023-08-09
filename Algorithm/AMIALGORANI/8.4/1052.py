n, k = map(int, input().split())
cnt = 0
while k < bin(n)[2:].count('1'):
    n += 1
    cnt += 1
print(cnt)
