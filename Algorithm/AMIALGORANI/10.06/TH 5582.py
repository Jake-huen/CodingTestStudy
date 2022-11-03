a = input()
b = input()
d = [[0 for _ in range(len(b))] for _ in range(len(a))]
temp=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            if i==0 or j==0:
                # print(i,j)
                d[i][j]=1
            else:
                d[i][j] = d[i-1][j-1]+1
            temp = max(temp,d[i][j])
print(temp)

# 실패한 코드
# for i in range(len(a)):
#     start = a[i]
#     b_start=0
#     b_start = b.find(start)
#     if b_start!=-1:
#         temp=0
#         a_check=0
#         for j in range(b_start,len(b)):
#             if i+a_check<len(a):
#                 if b[j]==a[i+a_check]:
#                     temp+=1
#                     a_check+=1
#                 else:
#                     break
#         d[i]=temp
#     while(b_start!=-1):
#         temp = 0
#         a_check = 0
#         b_start = b.find(start, b_start+1)
#         for j in range(b_start,len(b)):
#             if i + a_check < len(a):
#                 if b[j] == a[i + a_check]:
#                     temp += 1
#                     a_check += 1
#                 else:
#                     break
#         d[i]=max(d[i],temp)
# print(max(d))

