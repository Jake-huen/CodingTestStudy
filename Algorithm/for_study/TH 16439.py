from itertools import combinations
n,m = map(int,input().split()) #n:회원수 m:치킨 종류의 수
chicken=[]
for i in range(n):
    chicken.append(list(map(int,input().split())))
# print(chicken[0][3])
ans=0
# m 종류의 치킨 중에서 3가지 선택
cc=[]
for i in range(m):
    cc.append(i)
temp = list(combinations(cc,3))
# print(temp[0][0]) temp[i][0] temp[i][1] temp[i][2]

ans=[]
for i in range(len(temp)):
    bigyo = []
    temp2=0
    bigyo.append(temp[i][0])
    bigyo.append(temp[i][1])
    bigyo.append(temp[i][2])
    for j in range(n):
        temp2+=max(chicken[j][bigyo[0]],chicken[j][bigyo[1]],chicken[j][bigyo[2]])
    ans.append(temp2)
print(max(ans))