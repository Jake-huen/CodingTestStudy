#몸무게 x , 키 y (x,y)
n=int(input())
weight=[]
height=[]
sun=[]
for _ in range(n):
    x,y=map(int,input().split())
    weight.append(x)
    height.append(y)
def bigyo(a,b):
    if a<b:
        return True
    else:
        return False
for i in range(len(weight)):
    rank=1
    for j in range(len(weight)):
        if bigyo(weight[i],weight[j]):
            if bigyo(height[i],height[j]):
                rank+=1
    sun.append(rank)
for i in range(len(sun)):
    print(sun[i],end=' ')