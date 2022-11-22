import sys
input = sys.stdin.readline
n = int(input())
for _ in range(3):
    numbers = list(map(int, input().split()))
    dp=[0]*n
    dp[0]=numbers[0]

    for i in range(1, n):
        cur = 0
        min_p = 600000
        for j in range(i, -1, -1):
            cur += numbers[j]

            if j - 1 >= 0:
                more = cur - dp[j - 1]
            else:
                more = cur
            min_p = min(min_p, more)
        dp[i] = min_p
        print(dp)
    r = ''

    if dp[n - 1] > 0:
        r = 'B'
    elif dp[n - 1] < 0:
        r = 'A'
    else:
        r = 'D'
    print(r)