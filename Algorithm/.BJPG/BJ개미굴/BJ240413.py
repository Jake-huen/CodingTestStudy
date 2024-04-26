"""
각 층에 먹이가 있는 방을 따라 내려가다가 더 이상 내려갈 수 없으면 신호를 보냄
3
2 B A
4 A B C D
2 A C

A
--B
----C
------D
--C
B
--A
"""

n = int(input())

def add(dict, arr):
    if len(arr) == 0:
        return
    if arr[0] not in dict: # key로 존재하지 않으면 내려가야함
        dict[arr[0]] = {}
    add(dict[arr[0]], arr[1:]) # 하나씩 내려서 반복

def printTree(dict, l):
    for key in sorted(dict.keys()):
        print("--"*l + key)
        printTree(dict[key], l+1)


dict = {}

for _ in range(n):
    k = list(input().split(" "))
    add(dict, k[1:])
printTree(dict,0)
