n,m = map(int,input().split())
cards=list(map(int,input().split()))
answer=0
for i in cards:
    for j in cards:
        for k in cards:
            if i!=j and i!=k and j!=k:
                sum=i+j+k
                if sum>m:
                    continue
                else:
                    answer=max(answer,sum)
print(answer)