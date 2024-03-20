"""
기관차 1대가 객차 여러 칸
소형 기관차 3대 -> 기관차보다 적은 수의 객차
1. 소형 기관차 최대 객차 정해져 있음
2. 번호가 연속적으로 이어진 객차를 끌게 함
"""

n = int(input())
customers = list(map(int,input().split()))
max_limit = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]



# print(dp)