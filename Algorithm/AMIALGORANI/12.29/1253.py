n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    b = a[:i] + a[i + 1:]
    left = 0
    right = len(b) - 1
    while left < right:
        temp = b[left] + b[right]
        if temp == a[i]:
            ans += 1
            break
        if temp < a[i]:
            left += 1
        else:
            right -= 1
print(ans)

"""좋다
n개의 수 중에서 어떤 수가 다른 수 두개의 합으로 나타낼 수 있으면 좋다라고 함
"""
