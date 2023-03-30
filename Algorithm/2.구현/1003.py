import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero = [0] * (n + 3)
    one = [0] * (n + 3)
    zero[0] = 1
    one[1] = 1
    for i in range(2, n + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
    print(zero[n], one[n])
