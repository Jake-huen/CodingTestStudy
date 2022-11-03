t = int(input())
answer=[]
for _ in range(t):
    stickers=[]
    n = int(input())
    stickers.append(list(map(int,input().split()))) # 첫번째 라인
    stickers.append(list(map(int,input().split()))) # 두번째 라인
    d=[[0]*n for _ in range(2)]
    if n==1:
        answer.append(max(stickers[0][0],stickers[1][0]))
    else:
        d[0][0] = stickers[0][0]
        d[1][0] = stickers[1][0]
        d[0][1] = d[1][0]+stickers[0][1]
        d[1][1] = d[0][0]+stickers[1][1]
        for i in range(2,n):
            d[0][i]=max(d[1][i-1]+stickers[0][i],d[1][i-2]+stickers[0][i])
            d[1][i]=max(d[0][i-1]+stickers[1][i],d[0][i-2]+stickers[1][i])
        answer.append(max(d[0][n-1],d[1][n-1]))
for i in answer:
    print(i)