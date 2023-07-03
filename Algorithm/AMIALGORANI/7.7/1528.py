def recursion(num, A, B):
    global answer
    if num > 1_000_000_000:
        return

    if A <= num and num <= B:
        answer += 1
    recursion(10*num+4, A, B)
    recursion(10*num+7, A, B)

answer = 0
A = int(input())
B = int(input())
recursion(0, A, B)
print(answer)
