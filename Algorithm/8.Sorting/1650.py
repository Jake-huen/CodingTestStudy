n = int(input())

data=[]

for _ in range(n):
    x, y =list(map(int,input().split()))
    data.append((x,y))

data=sorted(data,key=lambda x:(x[0],x[1]))


for i in range(n):
    print(str(data[i][0])+' '+str(data[i][1]))