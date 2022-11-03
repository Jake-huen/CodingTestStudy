n = int(input())
numbers = list(map(int,input().split()))
d=[[0]*21 for _ in range(n-1)] # i번째 j나오는 수 -> d[i][j]
d[0][numbers[0]]=1
for i in range(1,n-1):
    for j in range(21):
        if d[i-1][j]!=0:
            plus_number = j+numbers[i]
            minus_number = j-numbers[i]
            if plus_number<=20:
                d[i][plus_number]+=d[i-1][j]
            if minus_number>=0:
                d[i][minus_number]+=d[i-1][j]
print(d[n-2][numbers[-1]])

