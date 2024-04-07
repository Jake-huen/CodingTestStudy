"""
1 X 9 = 9
2 X 90 = 180
3 X 900 = 2700
k가 어느 그룹에 들어가는지 알아야함.
"""

n, k = map(int, input().split())

start = 0
digit = 1
nine = 9

while k > nine * digit:
    k = k - (nine * digit)
    start = start + nine
    nine = nine * 10
    digit += 1
result = (start + 1) + (k - 1) // digit
if result > n:
    print(-1)
else:
    print(str(result)[(k - 1) % digit])
