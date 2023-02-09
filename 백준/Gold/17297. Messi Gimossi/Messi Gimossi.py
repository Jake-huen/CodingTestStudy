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