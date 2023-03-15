# def cantoa(array, start, now_length):
#     temp = now_length // 3
#     if temp == 0:
#         return
#     for i in range(start + temp, start + temp * 2):
#         array[i] = ' '
#     cantoa(array, start, temp)
#     cantoa(array, start + temp * 2, temp)
#
#
# while True:
#     try:
#         n = int(input())
#         if n == '':
#             break
#         else:
#             n = int(n)
#             array = ['-' for i in range(pow(3, n))]
#             cantoa(array, 0, pow(3, n))
#             ans = ""
#             for i in array:
#                 ans += i
#             print(ans)
#     except EOFError:
#         break
import sys
for i in sys.stdin:
    temp = "-"
    for j in range(int(i)):
        temp = temp + " " * len(temp) + temp
    print(temp)
