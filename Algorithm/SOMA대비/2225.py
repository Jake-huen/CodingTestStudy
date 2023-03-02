n, k = map(int, input().split())
sum = (n + 1) ** (k-1)
print(sum % 1000000000)
