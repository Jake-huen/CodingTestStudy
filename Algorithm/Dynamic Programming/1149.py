# RGB 거리

n = int(input())

d = []#입력받는 RGB거리 value의 값

r = []#각 집에서의 최솟값

check=[False]*3#전에 뭐가 들어갔는지 체크

for i in range(n):
    d.append(list(map(int, input().split())))

#r[0]=min(d[0][0],d[0][1],d[0][2])


