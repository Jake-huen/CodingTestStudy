n = int(input()) # 목표 채널
m = int(input())
if m!=0: # 세번째 줄이 없을 수도 있음
    errors = list(input().split())
else:
    errors=list()
answer = abs(n-100)
for num in range(1000001):
    for check in str(num):
        if check in errors: # 못만드는 경우
            break
    else:
        answer = min(answer,len(str(num))+abs(num-n))
print(answer)