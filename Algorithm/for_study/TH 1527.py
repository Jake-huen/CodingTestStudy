from itertools import product
a,b=map(int,input().split())
cnt=0
for i in range(len(str(a)),len(str(b))+1):
    temp=list(product([4,7],repeat=i))
    for j in temp:
        temp= ''.join(map(str,j))
        temp=int(temp)
        if temp>=a and temp<=b:
            cnt+=1
print(cnt)