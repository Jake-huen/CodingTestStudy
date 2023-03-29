from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    blank = [" ", "+", "-"]
    ways = list(product(blank, repeat=n - 1))
    answers = []
    for way in ways:
        temp = ''
        for i in range(1, n + 1):
            temp += str(i)
            if i != n:
                temp += way[i - 1]
        answers.append(temp)
    for answer in answers:
        temp = answer.replace(' ', '')
        if eval(temp) == 0:
            print(answer)
    print()
