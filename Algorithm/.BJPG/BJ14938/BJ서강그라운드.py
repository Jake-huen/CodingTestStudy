"""
낙하산에서 떨어질 때 각 지역에 아이템들이 몇 개 있는지 알려주는 프로그램
"""
n, m, r = map(int, input().split())
t = list(map(int, input().split()))
for _ in range(r):
    a, b, l = map(int, input().split())
