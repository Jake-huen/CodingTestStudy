n = int(input())
numbers = list(map(int, input().split()))
if n == 1:
    print("A")
elif n == 2:
    if numbers[1] == numbers[0]:
        print(numbers[0])
    else:
        print("A")
else:
    if numbers[0] == numbers[1]:
        a = 0
    else:
        a = (numbers[1] - numbers[2]) // (numbers[0] - numbers[1])
    b = numbers[1] - numbers[0] * a

    for i in range(n - 1):
        expect = numbers[i] * a + b
        if (numbers[i + 1] != expect):
            print("B")
            exit()
    print(numbers[-1] * a + b)

"""
다음 수 = 앞의 수 * a + b
다음 수 여러 개 -> A
다음 수 못구할 때 -> B
"""
