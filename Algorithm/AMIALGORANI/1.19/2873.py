import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))


def minGraph():
    x = 0
    y = 0
    ans = 1001
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1:
                if graph[i][j] <= ans:
                    ans = graph[i][j]
                    x = i
                    y = j
    return x, y


def happy(r, c):
    if (r % 2 == 1 and c % 2 == 1) or (r % 2 == 1 and c % 2 == 0):
        answer = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1)
        return answer
    elif r % 2 == 0 and c % 2 == 1:
        answer = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1)
        return answer
    else:
        a, b = minGraph()  # 못가는곳
        check = False
        answer = ''
        for i in range(0, r, 2):
            if not check:
                if a == i:
                    for j in range(1, c, 2):
                        if b == j:
                            answer += 'DR'
                            check = True
                        else:
                            if not check:
                                answer += 'DRUR'
                            else:
                                answer += 'RURD'
                    answer += 'D'
                elif a == i + 1:
                    for j in range(0, c, 2):
                        if b == j:
                            answer += 'RD'
                        else:
                            if not check:
                                answer += 'DRUR'
                            else:
                                answer += 'RDRU'
                    answer += 'D'
                else:
                    answer += ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D')
            else:
                answer += ('L' * (c - 1) + 'D' + 'R' * (c - 1) + 'D')
        return answer[:-1]


print(happy(r, c))
