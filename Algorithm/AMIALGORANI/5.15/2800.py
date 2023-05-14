from itertools import combinations


def concatsick(n, temp):
    ans = ''
    for i in range(len(n)):
        if i not in temp and i not in temp:
            ans += n[i]
    return ans


sick = list(input())
gwalhos = []
stack = []
for i in range(len(sick)):
    if sick[i] == '(':
        stack.append(i)
    elif sick[i] == ')':
        gwalhos.append([stack.pop(), i])
answers = set()
for i in range(1, len(gwalhos) + 1):
    ways = combinations(gwalhos, i)
    for way in ways:
        temp = []
        for i in range(len(way)):
            temp.append(way[i][0])
            temp.append(way[i][1])
        answers.add(concatsick(sick, temp))
answers = sorted(list(answers))
for answer in answers:
    print(answer)
# (0/(0))
# (0/0)
# 0/(0)
# 0/0
