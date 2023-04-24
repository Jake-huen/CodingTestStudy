import math

n = int(input())
temp = sorted([int(input()) for _ in range(n)])
numbers = []
for i in range(1, n):
    numbers.append(temp[i] - temp[i - 1])
gcd = numbers[0]
for number in numbers:
    gcd = math.gcd(gcd, number)
result = []
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
result.append(gcd)
print(*sorted(list(set(result))))
