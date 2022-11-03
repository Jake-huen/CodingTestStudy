#도시 : n*m 집:(1,1) 학원:(N,M) 오락실:C개
#현재 위치 : (r,c)
orac=[]
n,m,c = map(int,input().split())
for _ in range(c):
    x,y = map(int,input().split())
    orac.append((x,y))

