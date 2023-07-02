n = int(input())
if n <= 7:
    d = [-1] * 8
    d[4] = 1
    d[7] = 1
else:
    d = [-1] * (n + 1)
    d[4] = 1
    d[7] = 1
    for i in range(7, n + 1):
        case1, case2 = 0, 0
        if d[i - 4] >= 1:
            case1 = d[i - 4] + 1
        if d[i - 7] >= 1:
            case2 = d[i - 7] + 1
        if case1 ==0 and case2==0:
            d[i] = -1
        elif case1 == 0 and case2 != 0:
            d[i] = case2
        elif case1 != 0 and case2 == 0:
            d[i] = case1
        else:
            d[i] = min(case1, case2)
print(d[n])
