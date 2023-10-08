from itertools import product
from copy import deepcopy

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def move_left(graph):
    new_graph = graph.copy()
    for i in range(n):
        start_index = 0
        next_index = start_index + 1
        while next_index < n:
            if new_graph[i][start_index] == new_graph[i][next_index]:
                new_graph[i][start_index] = new_graph[i][start_index] + new_graph[i][next_index]
                new_graph[i][next_index] = 0
                start_index = next_index + 1
                next_index = start_index + 1
                if start_index > n or next_index > n:
                    break
            else:
                if new_graph[i][next_index] == 0:
                    next_index += 1
                    if next_index > n:
                        break
                else:
                    start_index = next_index
                    next_index = start_index + 1
                    if start_index > n or next_index > n:
                        break
        temp = new_graph[i]
        zero = []
        for j in range(n):
            if temp[j] == 0:
                zero.append(j)
            else:
                if zero:
                    new_graph[i][zero.pop(0)] = new_graph[i][j]
                    new_graph[i][j] = 0
                    zero.append(j)
    return new_graph


def move_right(graph):
    new_graph = graph.copy()
    for i in range(n):
        start_index = n - 1
        next_index = start_index - 1
        while next_index >= 0:
            if new_graph[i][start_index] == new_graph[i][next_index]:
                new_graph[i][start_index] = new_graph[i][start_index] + new_graph[i][next_index]
                new_graph[i][next_index] = 0
                start_index = next_index - 1
                next_index = start_index - 1
                if start_index <= 0 or next_index < 0:
                    break
            else:
                if new_graph[i][next_index] == 0:
                    next_index -= 1
                    if next_index < 0:
                        break
                else:
                    start_index = next_index
                    next_index = start_index - 1
                    if start_index <= 0 or next_index < 0:
                        break
        temp = new_graph[i]
        zero = []
        for j in range(n - 1, -1, -1):
            if temp[j] == 0:
                zero.append(j)
            else:
                if zero:
                    new_graph[i][zero.pop(0)] = new_graph[i][j]
                    new_graph[i][j] = 0
                    zero.append(j)
    return new_graph


def move_up(graph):
    new_graph = graph.copy()
    for i in range(n):
        start_index = 0
        next_index = start_index + 1
        while next_index < n:
            if new_graph[start_index][i] == new_graph[next_index][i]:
                new_graph[start_index][i] = new_graph[start_index][i] + new_graph[next_index][i]
                new_graph[next_index][i] = 0
                start_index = next_index + 1
                next_index = start_index + 1
                if start_index > n or next_index > n:
                    break
            else:
                if new_graph[next_index][i] == 0:
                    next_index += 1
                    if next_index > n:
                        break
                else:
                    start_index = next_index
                    next_index = start_index + 1
                    if start_index > n or next_index > n:
                        break
        zero = []
        for j in range(n):
            if new_graph[j][i] == 0:
                zero.append(j)
            else:
                if zero:
                    new_graph[zero.pop(0)][i] = new_graph[j][i]
                    new_graph[j][i] = 0
                    zero.append(j)
    return new_graph


def move_down(graph):
    new_graph = graph.copy()
    for i in range(n):
        start_index = n - 1
        next_index = start_index - 1
        while next_index >= 0:
            if new_graph[start_index][i] == new_graph[next_index][i]:
                new_graph[start_index][i] = new_graph[start_index][i] + new_graph[next_index][i]
                new_graph[next_index][i] = 0
                start_index = next_index - 1
                next_index = start_index - 1
                if start_index <= 0 or next_index < 0:
                    break
            else:
                if new_graph[next_index][i] == 0:
                    next_index -= 1
                    if next_index < 0:
                        break
                else:
                    start_index = next_index
                    next_index = start_index - 1
                    if start_index <= 0 or next_index < 0:
                        break
        zero = []
        for j in range(n - 1, -1, -1):
            if new_graph[j][i] == 0:
                zero.append(j)
            else:
                if zero:
                    new_graph[zero.pop(0)][i] = new_graph[j][i]
                    new_graph[j][i] = 0
                    zero.append(j)
    return new_graph


ways = product([0, 1, 2, 3], repeat=5)
ans = 0
for way in ways:
    temp = deepcopy(graph)
    for i in way:
        if i == 0:
            temp = move_left(temp)
        elif i == 1:
            temp = move_right(temp)
        elif i == 2:
            temp = move_up(temp)
        elif i == 3:
            temp = move_down(temp)
    for i in range(n):
        for j in range(n):
            ans = max(ans, temp[i][j])
print(ans)
'''
1. 반복할때 permutation 사용하는 부분 -> DFS로도 해결 가능
2. left랑 right는 다르다
3. 백트래킹의 개념과 활용법
    해를 찾는 도중에 막히면 더 이상 깊이 들어가지 않고, 이전 단계로 되돌아가서 해를 찾아나가는 기법.
4. DeepCopy의 개념과 copy와의 차이점
'''
