import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int,input().split()))
# 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀
# 시작한 장소에서는 꿀을 딸 수 없다.

#경우가 3가지가 있음
# 벌 벌 꿀
# 벌 꿀 벌
# 꿀 꿀 벌
answer=0
sub_honey=[]
sub_honey.append(honey[0])

for i in range(1,n):
    sub_honey.append(sub_honey[i-1]+honey[i])

# 벌 벌 꿀
for i in range(1,n-1):
    answer = max(answer,2*sub_honey[-1]-honey[0]-honey[i]-sub_honey[i])


# 꿀 벌 벌
for i in range(1,n-1):
    answer = max(answer,sub_honey[-1]-honey[-1]-honey[i]+sub_honey[i-1])
# 벌 꿀 벌
for i in range(1,n-1):
    answer = max(answer,sub_honey[i]-honey[0]+sub_honey[-1]-sub_honey[i-1]-honey[-1])

print(answer)