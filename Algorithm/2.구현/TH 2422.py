#1~N까지
n,m = map(int,input().split())
#n은 아이스크림 종류의 수,, m은 섞어먹으면 안되는 조합의 개수
johap = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    i1,i2 = map(int, input().split())
    johap[i1-1][i2-1] = True
    johap[i2-1][i1-1] = True
answer=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if not johap[i][j] and not johap[i][k] and not johap[j][k]:
                answer += 1
print(answer)