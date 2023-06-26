# 투 포인터 사용하기
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_pointer, b_pointer = 0, 0
a_length, b_length = len(a), len(b)

answer = []
while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:
        answer.append(b[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:
        answer.append(a[a_pointer])
        a_pointer += 1
    else:
        if a[a_pointer] > b[b_pointer]:
            answer.append(b[b_pointer])
            b_pointer += 1
        else:
            answer.append(a[a_pointer])
            a_pointer += 1
print(*answer)
