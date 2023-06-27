n = int(input())
a = list(map(int, input().split()))

a.sort()

minus_pointer = 0
plus_pointer = n - 1

check = 1000000000
answer = []

while minus_pointer < plus_pointer:
    temp_minus = a[minus_pointer]
    temp_plus = a[plus_pointer]
    total = temp_minus + temp_plus
    if abs(total) < check:
        check = abs(total)
        answer = [temp_minus, temp_plus]
    if total < 0:
        minus_pointer += 1
    else:
        plus_pointer -= 1
print(answer[0], answer[1])
