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
            if not isEmpty(nums.items()):
                if n==1: # 최댓값을 삭제
                    while -max_q[0] not in nums or nums[-max_q[0]] <1:
                        temp = -heappop(max_q)
                        if temp in nums:
                            del(nums[temp])
                elif n==-1: # 최솟값을 삭제
                    while min_q[0] not in nums or nums[min_q[0]] < 1:
                        temp = heappop(min_q)
                        if temp in nums:
                            del (nums[temp])
                    nums[min_q[0]] -= 1
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_q[0] not in nums or nums[min_q[0]] < 1:
            heappop(min_q)
        while -max_q[0] not in nums or nums[-max_q[0]] < 1:
            heappop(max_q)
        print(-max_q[0], min_q[0])
