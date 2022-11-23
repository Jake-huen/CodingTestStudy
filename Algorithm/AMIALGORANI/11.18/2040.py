import sys
input = sys.stdin.readline

n = int(input())
for _ in range(3):
    numbers = list(map(int, input().split()))
    a=0
    b=0
    for i in range(n):
        temp = numbers[i]
        a1 = temp+a
        b1 = b
        a2 = temp+b
        b2 = a
        # print("a1 ",a1,"a2 ",a2,"b1 ",b1,"b2 ",b2)
        if a1-b1 <= a2-b2:
            a = a1
            b = b1
        else:
            a = a2
            b = b2
        # print("비교 후")
        # print("a ", a, "b ", b)
        # print()
    if a<b:
        print('A')
    elif a>b:
        print('B')
    else:
        print('D')
