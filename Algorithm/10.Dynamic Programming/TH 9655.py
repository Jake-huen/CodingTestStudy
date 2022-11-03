# 돌 게임
n = int(input())
d=[-1]*(n+1)
#print(d)
# for i in range(n+1):
#     if i==1 or i==3:
#         d[i]=1 #1이면 상근
#     elif i==2:
#         d[i]=0 #0이면 창영
#     else:
#         if i%2==0:#창영
#             if d[i-1]==0 or d[i-3]==0:
#                 d[i]=0
#             else:
#                 d[i]=1
#         elif i%2==1:#상근
#             if d[i-1]==1 or d[i-3]==1:
#                 d[i]=1
#             else:
#                 d[i]=0
if n%2==1:
    print("SK")
elif n%2==0:
    print("CY")
