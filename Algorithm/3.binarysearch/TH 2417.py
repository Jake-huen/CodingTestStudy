# n= int(input())
# 시작 : 0, 끝: n
# start = 0
# end = n
# ans=0
# while start<=end:
#     mid=(start+end)//2
#     if mid*mid<n:
#         start=mid+1
#     elif mid*mid>=n:
#         end=mid-1
# # print(start,end,end='       ')
# print(start)
n = int(input())
num = n

def findSqrt(start, end) :
    if start==0:
        return 0
    q = (start + end) // 2
    if q**2 >= num:
        if (q - 1)**2 < num:
            return q
        else:
            return findSqrt(start, q - 1)
    else :
        return findSqrt(q + 1, end)


print(findSqrt(0, n))