n = int(input())
d = ['None'] * (n + 1)
if n == 1:
    print("CY")
elif n == 2:
    print("SK")
elif n == 3:
    print("CY")
else:
    d[1] = "CY"
    d[2] = "SK"
    d[3] = "CY"
    for i in range(4, n + 1):
        if d[i - 1] == 'SK' and d[i - 3] == "SK":
            d[i] = "CY"
        else:
            d[i] = "SK"
    print(d[n])

"""
n = 1 : CY
n = 2 : SK
n = 3 : CY
"""
