n = list(input())


def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
def allsame(n):
    check = n[0]
    for i in range(1,len(n)):
        if n[i] != check:
            return False
    return True

if palindrome(n):
    if allsame(n):
        print(-1)
    else:
        print(len(n) - 1)
else:
    print(len(n))