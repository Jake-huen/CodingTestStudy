import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    ans = 10000000
    ans_num = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            temp = s[i] + s[mid]
            if abs(k - temp) < ans:
                ans = abs(k - temp)
                ans_num = 1
            elif abs(k - temp) == ans:
                ans_num += 1
            if temp > k:
                right = mid - 1
            else:
                left = mid + 1
    print(ans_num)
