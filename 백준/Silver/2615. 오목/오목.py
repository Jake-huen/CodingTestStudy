from collections import deque

graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))


# 검 : 1, 흰 : 2

def garo(x, y):
    check = graph[x][y]
    if y - 1 >= 0:
        if graph[x][y - 1] == check:
            return False
    if y + 5 < 19:
        if graph[x][y + 5] == check:
            return False
    if y + 4 < 19:
        for i in range(1, 5):
            if check != graph[x][y + i]:
                return False
    else:
        return False
    return True


def sero(x, y):
    check = graph[x][y]
    if x - 1 >= 0:
        if graph[x - 1][y] == check:
            return False
    if x + 5 < 19:
        if graph[x + 5][y] == check:
            return False
    if x + 4 < 19:
        for i in range(1, 5):
            if check != graph[x + i][y]:
                return False
    else:
        return False
    return True


def dkright(x, y):
    check = graph[x][y]
    if x - 1 >= 0 and y - 1 >= 0:
        if graph[x - 1][y - 1] == check:
            return False
    if x + 5 < 19 and y + 5 < 19:
        if graph[x + 5][y + 5] == check:
            return False
    if x + 4 < 19 and y + 4 < 19:
        for i in range(1, 5):
            if check == graph[x + i][y + i]:
                continue
            else:
                return False
    else:
        return False
    return True


def dkleft(x, y):
    check = graph[x][y]
    if x - 1 >= 0 and y + 1 < 19:
        if graph[x - 1][y + 1] == check:
            return False
    if x + 5 < 19 and y - 5 >= 0:
        if graph[x + 5][y - 5] == check:
            return False
    if x + 4 < 19 and y - 4 >= 0:
        for i in range(1, 5):
            if check == graph[x + i][y - i]:
                continue
            else:
                return False
    else:
        return False
    return True


for i in range(19):
    for j in range(19):
        if graph[i][j] == 1:  # 검
            if garo(i, j) or sero(i, j) or dkright(i, j):
                print(1)
                print(i + 1, j + 1)
                #print(garo(i,j),sero(i,j),dkright(i,j))
                exit()
            if dkleft(i, j):
                print(1)
                print(i + 5, j - 3)
                #print("df",dkleft(i,j))
                exit()
        elif graph[i][j] == 2:  # 흰
            if garo(i, j) or sero(i, j) or dkright(i, j):
                print(2)
                print(i + 1, j + 1)
                #print(garo(i, j), sero(i, j), dkright(i, j))
                exit()
            if dkleft(i, j):
                print(2)
                print(i + 5, j - 3)
                #print("df",dkleft(i,j))
                exit()
print(0)
