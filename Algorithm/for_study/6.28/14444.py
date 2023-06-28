s = list(input())


def palindrome(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


result = 0
for i in range(len(s) - 1):
    result = max(result, palindrome(i, i + 1), palindrome(i, i + 2))
print(result)
