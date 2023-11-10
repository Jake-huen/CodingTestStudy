import sys

read = sys.stdin.readline

n, k = map(int, read().split())

num_arr = [0] * 1024

for _ in range(n):
    num_str = read().rstrip()
    bit_str = ['0'] * 10
    for c in num_str:
        bit_str[int(c)] = '1'
    bit_str = ''.join(bit_str)
    num_arr[int(bit_str, 2)] += 1

ans = 0

for i in range(1024):
    if num_arr[i] == 0:
        continue

    for j in range(i, 1024):
        if num_arr[j] == 0:
            continue
        if str(bin(i | j)).count('1') == k:
            if i == j and num_arr[i] > 1:
                n = num_arr[i]
                ans += n * (n - 1) / 2
            elif i != j:
                ans += num_arr[i] * num_arr[j]

print(int(ans))
