# 톱니바퀴 N극은 0, S극은 1
one = list(map(int, input()))
two = list(map(int, input()))
three = list(map(int, input()))
four = list(map(int, input()))

topni = []
topni.append(one)
topni.append(two)
topni.append(three)
topni.append(four)
k = int(input())  # 회전시키는 방법


def turn_left(line):  # 시계 반대방향으로 회전
    # 1번 2번 3번 .... 0번
    new_line = []
    for i in range(1, len(line)):
        new_line.append(line[i])
    new_line.append(line[0])
    return new_line


def turn_right(line):  # 시계 방향으로 회전
    # -1번 0번 1번 ...
    new_line = []
    for i in range(-1, len(line) - 1):
        new_line.append(line[i])
    return new_line


score = 0
for _ in range(k):
    num, dir = map(int, input().split())  # 회전시키는 번호, 정수 방향
    if num == 1:
        temp = [dir, 0, 0, 0]
        if topni[0][2] != topni[1][-2]:
            temp[1] = -temp[0]
            if topni[1][2] != topni[2][-2]:
                temp[2] = -temp[1]
                if topni[2][2] != topni[3][-2]:
                    temp[3] = -temp[2]
        for i in range(len(temp)):
            if temp[i] == -1:
                topni[i] = turn_left(topni[i])
            elif temp[i] == 1:
                topni[i] = turn_right(topni[i])
    elif num == 2:
        temp = [0, dir, 0, 0]
        if topni[1][2] != topni[2][-2]:
            temp[2] = -temp[1]
            if topni[2][2] != topni[3][-2]:
                temp[3] = -temp[2]
        if topni[1][-2] != topni[0][2]:
            temp[0] = -temp[1]
        for i in range(len(temp)):
            if temp[i] == -1:
                topni[i] = turn_left(topni[i])
            elif temp[i] == 1:
                topni[i] = turn_right(topni[i])

    elif num == 3:
        temp = [0, 0, dir, 0]
        if topni[2][2] != topni[3][-2]:
            temp[3] = -temp[2]
        if topni[2][-2] != topni[1][2]:
            temp[1] = -temp[2]
            if topni[0][2] != topni[1][-2]:
                temp[0] = -temp[1]
        for i in range(len(temp)):
            if temp[i] == -1:
                topni[i] = turn_left(topni[i])
            elif temp[i] == 1:
                topni[i] = turn_right(topni[i])

    elif num == 4:
        temp = [0, 0, 0, dir]
        if topni[2][2] != topni[3][-2]:
            temp[2] = -temp[3]
            if topni[1][2] != topni[2][-2]:
                temp[1] = -temp[2]
                if topni[0][2] != topni[1][-2]:
                    temp[0] = -temp[1]
        for i in range(len(temp)):
            if temp[i] == -1:
                topni[i] = turn_left(topni[i])
            elif temp[i] == 1:
                topni[i] = turn_right(topni[i])

for i in range(4):
    if topni[i][0] == 1:
        score += 2 ** i
print(score)
