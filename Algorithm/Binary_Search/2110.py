n,c = map(int,input().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()
start =1
end = house[-1]-house[0]
ans=0
while start<=end:
    mid = (start+end)//2
    cnt = 1#이 부분이 이해가 안감 : 아래 해설
    begin_house=house[0]
    for i in range(1,n):
        if begin_house+mid<=house[i]:
            begin_house=house[i]
            cnt+=1
    if cnt>=c:#거리를 더 키워도 됨
        ans=mid
        start=mid+1
    elif cnt<c:
        end=mid-1
print(ans)
#첫번째 집에 항상 공유기가 존재해야 하는 이유
#첫번째 집에 설치해야 손해를 보지 않는다. 최적으로 되도록 공유기를 c개 설치했는데
#첫 번째 집 설치를 안해놓았다고 하자. 맨 왼쪽에 설치된 공유기를 첫번쨰 집에 설치하면
#거리가 늘기만 하지 줄지는 않는다. 최적의 해를 구하는데 굳이 첫번째 집에 설치를 안할
#이유가 없는것이다.