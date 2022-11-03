n = int(input())
candy = []
for i in range(n):
    candy.append(list(input()))
# print(candy)
def check(candy):
    ans=1
    for i in range(len(candy)):
        cnt=1
        for j in range(1,len(candy)):
            if candy[i][j]==candy[i][j-1]:
                cnt+=1
            else:
                cnt=1
            if cnt>ans:
                ans=cnt
        cnt=1
        for j in range(1,len(candy)):
            if candy[j][i]==candy[j-1][i]:
                cnt+=1
            else:
                cnt=1
            if cnt>ans:
                ans=cnt
    return ans
answer=0
for i in range(n):
    for j in range(n):
        if j+1<n:
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
            temp = check(candy)
            if temp>answer:
                answer=temp
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
        if i+1<n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            temp=check(candy)
            if temp>answer:
                answer=temp
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
print(answer)