s = int(input())
s = int(input())
tmp=0
ans=0
for i in range(s):
    tmp+=i
    if tmp>s:
        break
    ans += 1
print(ans-1)
# n=0
# def findNum(start, end):
#     n=(start+end)//2
#     if (n*(n+1))//2==s:
#         return n
#     elif(n*(n+1))//2<s:
#         findNum(start,n-1)
#     else:
#         findNum(n+1,end)
#     return -1
# print(findNum(1,s))