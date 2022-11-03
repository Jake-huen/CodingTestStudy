# N X M (n-1,m-1)
N,M = map(int,input().split())
if N==1:
    print(1)
elif N==2:
    print(min(4,(M+1)//2))
else:
    if M>=6:
        print(M-2)
    elif M<4:
        print(M)
    elif M>=4 and M<6:
        print(4)
# current=[(0,0)]
# dx = [2,1,-1,-2]
# dy = [1,2,2,1]
# temp = 1
# while current:
#     x, y = current.pop()
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx>=0 and ny>=0 and nx<N and ny<M:
#             current.append((nx,ny))
#             temp+=1
#             break
#         else:
#             continue
# print(temp)