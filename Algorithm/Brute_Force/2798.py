n,m = map(int,input().split())
cards=list(map(int,input().split()))
def find():
    sum = 0
    for i in cards:
        for j in cards:
            for k in cards:
                sum=i+j+k
                if sum==m:
                    answer=sum
                    print(answer)
                    return
find()


