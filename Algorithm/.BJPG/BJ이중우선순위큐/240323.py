from heapq import heappush, heappop
import sys

input = sys.stdin.readline

"""
데이터를 삭제할 때 연산 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나 삭제
"""

def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

t = int(input())
for _ in range(t):
    k = int(input())  # Q에 적용할 연산 개수
    max_q = []
    min_q = []
    nums = dict()
    for _ in range(k):
        op, n = map(str, input().split())
        n = int(n)
        if op == 'I':
            heappush(max_q, -n)
            heappush(min_q, n)
        elif op == 'D':
            if n==1: # 최댓값을 삭제

            elif n==-1: # 최솟값을 삭제

