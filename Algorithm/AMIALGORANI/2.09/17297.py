def Messi(idx, m):
    if idx <= 1:
        return "Messi Gimossi"[m - 1]
    if m > dp[idx - 1] + 1:
        return Messi(idx - 2, m - dp[idx - 1] - 1)
    elif m < dp[idx - 1]:
        return Messi(idx - 1, m)
    else:
        return " "


m = int(input())
dp = [5, 13]
while True:
    if dp[-1] >= m:
        break
    dp.append(dp[-1] + dp[-2] + 1)
ans = Messi(len(dp) - 1, m)
if ans == " ":
    print("Messi Messi Gimossi")
else:
    print(ans)

'''
n->1 f(1)                                                               1 m             5                  = 5
n->2 f(2)                                                               2 mg            5+1+7              = 13
n->3 f(2) + f(1)                                                        2 1 mgm         5+1+7+1+5          = 19 => 5+1+13
n->4 f(3) + f(2) = f(2) + f(1) + f(2)                                   2 1 2 mgmmg     5+1+7+1+5+1+5+1+7  = 33 => 5+1+13+1+13
n->5 f(4) + f(3) = f(2) + f(1) + f(2) + f(2) + f(1)                     2 1 2 2 1                                             1+5+1+13
n->6 f(5) + f(4) = f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2)2 1 2 2 1 2 1 2                                                 1+5+1+13+1+13
n->7 f(6) + f(5) = f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2) + f(4) + f(3) = f(2) + f(1) + f(2) + f(2) + f(1)2 1 2 2 1 2 1 2 2 1 2 2 1
2는 길이가 13, 1은 길이가 5

m이 어디에 속하는지 알아야 한다.
'''
