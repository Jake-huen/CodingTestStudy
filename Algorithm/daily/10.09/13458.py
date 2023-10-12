n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0

for student in a:
    student = student - b
    ans += 1
    if student > 0:
        ans += (student // c)
        if student % c != 0:
            ans += 1
print(ans)
