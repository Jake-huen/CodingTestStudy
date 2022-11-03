#x의 각 자리가 등차수열을 이룬다 -> 한수
#n이 주어졌을 때 1<=N 의 한수의 개수 출력
n = int(input())
count=0
for i in range(1,n+1):
    x=[]
    for j in str(i):
        x.append(int(j))
    if len(x)==1 or len(x)==2:
        count+=1
    else:
        if x[0]-x[1]==x[1]-x[2]:
            count+=1
print(count)


