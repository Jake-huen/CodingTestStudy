"""
각 층에 먹이가 있는 방을 따라 내려가다가 더 이상 내려갈 수 없으면 신호를 보냄
"""

n = int(input())
food_info = []
for _ in range(n):
    k = list(input().split(" "))
    food_info.append(k[1:])
print(food_info)