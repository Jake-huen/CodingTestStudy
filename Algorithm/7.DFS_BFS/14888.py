import sys
n = int(input())
data=list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

min_value = sys.maxsize
max_value = -sys.maxsize+1

def dfs(i,now):
    global min_value,max_value,add,sub,mul,div
    if i==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/data[i]))
            div+=1
dfs(1,data[0])
print(max_value)
print(min_value)

# 식을 만들 수 있는 경우의 수를 모두 조합하여 나온 결과값을 비교하는 브루트포스 방식
# 1. itertools의 permutations을 활용하여 순서를 고려한 모든 경우의 수를 구해 최대값과 최소값을 계산
# -> 라이브러리를 사용하면 코드가 간단해지고 구현하기가 쉽지만, 채점에서 시간이 걸린다.
# 2. 재귀를 활용해 모든 겨우의 수를 고려하여 최대값과 최소값을 계산한다.
# from itertools import permutations
# from collections import deque
# import copy
# # 파이썬은 레퍼런스 copy이기 때문에 리스트를 복사해서 해결하여야 한다 -> copy에서 동일하게 동작가능
# import sys
#
# def solve(n,num_list,operation_count_list):
#     op = ['+','-','*','//']
#     operation_list = []
#     max = -sys.maxsize-1
#     min = sys.maxsize
#     for i in range(4):
#         operation = op[i]
#         count = operation_count_list[i]
#         temp = [operation]*count
#         operation_list.extend(temp)
#         # extend 와 append의 차이점
#         # append는 x 그 자체를 원소로 넣고
#         # extend는 iterable의 각 항목들을 넣는다.
#     case_list = set(permutations(operation_list,n-1))
#
#     for case in case_list:
#         temp_list = deque(copy.deepcopy(num_list))
#         idx=-1
#         result=temp_list.popleft()
#         while temp_list:
#             idx+=1
#             next_num = temp_list.popleft()
#             current_op=case[idx]
#
#             if current_op=='+':
#                 result+=next_num
#             elif current_op=='-':
#                 result-=next_num
#             elif current_op=='*':
#                 result*=next_num
#             else:
#                 if result<0:
#                     result=-(result)
#                     result//=next_num
#                     result=-(result)
#                 else:
#                     result//=next_num
#         if result<min:
#             min=result
#         if max<result:
#             max=result
#     return max,min
#
#
#
# if __name__ == "__main__":
#     n = int(input())
#     num_list = deque(list(map(int,input().strip().split())))
#     operation_count_list = deque(list(map(int,input().strip().split())))
#
#     max,min = solve(n,num_list,operation_count_list)
#     print(max)
#     print(min)































