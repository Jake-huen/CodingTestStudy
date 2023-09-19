import math

n = int(input())


# 메모리 4MB
def sosu(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def dfs(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(10):
            temp = x * 10 + i
            if sosu(temp):
                dfs(temp)
dfs(2)
dfs(3)
dfs(5)
dfs(7)
