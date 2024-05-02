"""
N개의 방. 각각의 방에는 한개의 컴퓨터. 각각의 컴퓨터는 랜선으로 연결.

A, B가 있을 때 서로 랜선으로 연결되어 있거나, 다른 컴퓨터를 통해서 연결이 되어있으면 서로 통신을 할 수 있다.

N개의 컴퓨터 모두 연결하고싶음.

a부터 z는 1부터 26 / A부터 Z는 27부터 52.

컴퓨터 i와 j를 연결하는 것.

기부할 수 있는 랜선의 최대값 출력
3
abc
def
ghi

40

2
a0
0b

-1
4
0X00
00Y0
0000
00Z0

0
"""


def char_to_custom_number(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1  # 소문자 'a'는 1, 'b'는 2, ..., 'z'는 26
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27  # 대문자 'A'는 27, 'B'는 28, ..., 'Z'는 52
    else:
        return 0


n = int(input())

graph = []
total = 0
for i in range(n):
    temp = list(input())
    for j in range(n):
        graph.append([char_to_custom_number(temp[j]), i, j])
        total += char_to_custom_number(temp[j])

parent = [i for i in range(n)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


graph.sort(key=lambda x: x[0])

for x in graph:
    cost, a, b = x
    if cost == 0:
        continue
    if find(a) != find(b):
        union(a, b)
        total -= cost
    else:
        continue
flag = True
for i in range(n):
    if find(i) != 0:
        flag = False
if flag:
    print(total)
else:
    print(-1)
