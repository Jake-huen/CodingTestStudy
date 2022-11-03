n = int(input())
tip=[]
for i in range(n):
    tip.append(int(input()))
# 생각했던 돈이 작으면 등수 미뤄도 될듯.
tip.sort(reverse=True)
answer=0
for i in range(n):
    temp = tip[i]-i
    if temp<0:
        temp=0
    answer+=temp
print(answer)