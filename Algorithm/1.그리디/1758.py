# 원래 생각했던 돈 - (받은 등수-1)
# 받을 수 있는 tip의 최대값
n = int(input())
tip = []
answer=0
for i in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)
for i in range(n):
    if (tip[i] - i)>0:
        answer+=(tip[i]-i)
print(answer)