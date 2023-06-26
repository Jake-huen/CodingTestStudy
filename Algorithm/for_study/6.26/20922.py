n, k = map(int, input().split())
a = list(map(int, input().split()))
d = [0] * (max(a) + 1)
start_pointer = 0
end_pointer = 0
answer = 0
while end_pointer < n:
    current = a[end_pointer]
    if d[current] < k:
        d[current] += 1
        end_pointer += 1
    else:
        d[a[start_pointer]] -= 1
        start_pointer += 1
    answer = max(answer, end_pointer - start_pointer)
print(answer)
