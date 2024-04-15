from collections import deque

n, m = map(int, input().split())
"""
빨간 구슬을 빼내는 게임
"""
board = []
for _ in range(n):
    board.append(list(input()))

