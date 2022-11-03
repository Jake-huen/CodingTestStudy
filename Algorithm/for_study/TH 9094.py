t= int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ans=0
    for i in range(1,n):
        for j in range(i+1,n):
            # print(i,j)
            temp = i**2+j**2+m
            temp_div = i*j
            # print(temp,temp_div)
            if temp%temp_div==0:
                ans+=1
    print(ans)