# from collections import deque
# from itertools import combinations
#
# a = input()
# b = input()
#
#
# def way1(temp, q):
#     ans = ''
#     if len(temp) > 0:
#         s = temp[1:]
#     else:
#         s = temp
#     for i in range(len(s)):
#         ans += s[i]
#     return ans
#
#
# def way2(temp):
#     cnt = 0
#     cp = '0'
#     for l in temp:
#         if l == '1':
#             cnt += 1
#     if cnt % 2 == 1:
#         cp = '1'
#     ans = ''
#     for i in range(len(temp)):
#         ans += temp[i]
#     ans += cp
#     return ans
#
#
# # q = deque()
# # q.append(a)
# # answer = []
# # for i in list(combinations(a, 4)):
# #     answer.append(''.join(i))
# # print(answer)
# #
# # print(q)
#
# # 처음에 a의 1의 개수가 홀수 -> 1은 한개 더 늘어날 수 있음, or 줄어듬
# # 처음에 a의 1의 개수가 짝수 -> 1은 유지, or 줄어듬
# count1 = a.count('1')
# count2 = b.count('1')
# if count1 >= count2:
#     print('VICTORY')
# elif count1 < count2:
#     if count1 % 2 == 1 and count1 + 1 == count2:
#         print('VICTORY')
#     else:
#         print('DEFEAT')
# '''
# 1100 1010 1001 0110 0101 0011
#
# 1001 -> 001 -> 01 -> 0 -> 1
#                     -> 011
#             -> 0011 -> 011 -> 11-> 1
#                     -> 00110 -> 0110 -> 110 ->
#     -> 10010
# '''
print('VDIECFTEOARTY'[eval('1'+'>-input().count("1")//2'*2)::2])