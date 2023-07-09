def containsOnly47(number):
    if number == 0:
        return False
    while number > 0:
        digit = number % 10
        if digit != 4 and digit != 7:
            return False
        number //= 10
    return True


def dfs(MaxCombnum, combarr, checkhow, now, _sum):
    if _sum > n:
        return
    elif MaxCombnum == now:
        if _sum == n:
            global minnum
            if minnum == n + 1:
                minnum = MaxCombnum
            global ret
            if ret is not None:
                for i in range(MaxCombnum - 1, -1, -1):
                    if ret[i] > combarr[i]:
                        for j in range(minnum - 1, 0, -1):
                            print(ret[j], end=" ")
                        print(ret[0])
                        for j in range(MaxCombnum - 1, 0, -1):
                            print(combarr[j], end=" ")
                        print(combarr[0])
                        for k in range(MaxCombnum):
                            ret[k] = combarr[k]
                        break
            else:
                ret = [0] * MaxCombnum
                for k in range(MaxCombnum):
                    ret[k] = combarr[k]
                return
        return
    for i in range(checkhow, -1, -1):
        if (MaxCombnum - now) * ar[i] + _sum >= n:
            combarr[now] = ar[i]
            dfs(MaxCombnum, combarr, i, now + 1, _sum + ar[i])
            combarr[now] = 0


n = int(input())
retcount = n
dp = [-1] * (n + 1)
ar = [0] * (n + 1)
count = 0
minnum = n + 1

for i in range(n + 1):
    if containsOnly47(i):
        ar[count] = i
        dp[i] = 1
        count += 1

for i in range(1, n + 1):
    if minnum > i:
        dfs(i, [0] * i, count - 1, 0, 0)

if ret is not None:
    for j in range(minnum - 1, 0, -1):
        print(ret[j], end=" ")
    print(ret[0])
else:
    print(-1)
