from itertools import product

n, k = map(int, input().split())
a = list(map(int, input().split()))
r = []
m = []
for _ in range(k):
    r.append(list(map(int, input().split())))
for _ in range(k):
    m.append(list(map(int, input().split())))
ways = []
temp = []
for i in range(n):
    temp.append(i)
for i in product(temp, repeat=k):
    ways.append(i)


def check(temp):
    for i in range(n):
        if temp[i] > a[i]:
            return False
    return True


answers = []
for way1 in ways:  # 랑이
    for way2 in ways:  # 메리
        temp = [0] * n
        answer = 0
        for i in range(k):
            temp[way1[i]] += 1
            answer += r[i][way1[i]]
        for i in range(k):
            temp[way2[i]] += 1
            answer += m[i][way2[i]]
        if check(temp):
            answers.append(answer)
print(max(answers))
