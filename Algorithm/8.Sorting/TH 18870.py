# X1, X2, X3, ... , XN
# Xi를 좌표 압축한 결과 Xi'은 Xi>Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
import sys
input = sys.stdin.readline
n = int(input())
xi=list(map(int,input().split()))

answer=[]
temp = sorted(list(set(xi)))

dict={temp[i]:i for i in range(len(temp))}
for i in range(n):
    print(dict[xi[i]],end=' ')

# print(temp)
# print(xi)
# for i in range(n):
#     ans=0
#     for j in range(n):
#         if xi[i]>temp[j]:
#             ans+=1
#         else:
#             break
#     answer.append(ans)
# for i in range(n):
#     print(answer[i],end=' ')