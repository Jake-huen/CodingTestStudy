# xkg ycm (x,y)
n = int(input())
height =[]
weight=[]
for i in range(n):
    x,y = map(int,input().split())
    height.append(x)
    weight.append(y)
answer=[]
for i in range(n):
    count=0
    for j in range(n):
        if i!=j:
            if height[i]<height[j] and weight[i]<weight[j]:
                count+=1
    answer.append(count+1)
for i in range(len(answer)):
    print(answer[i],end=' ')