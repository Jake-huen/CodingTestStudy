import sys
input = sys.stdin.readline

n = int(input())

minus=[]
plus=[]
answer=0

for i in range(n):
    temp = int(input())
    if temp>1:
        plus.append(temp)
    elif temp==1:
        answer+=1
    else:
        minus.append(temp)
plus = sorted(plus,reverse=True)
minus = sorted(minus)
if len(plus)%2==0:
    for i in range(0,len(plus),2):
        answer+=(plus[i]*plus[i+1])
else:
    for i in range(0,len(plus)-1,2):
        answer+=plus[i]*plus[i+1]
    answer+=plus[-1]
if len(minus)%2==0:
    for i in range(0,len(minus),2):
        answer+=minus[i]*minus[i+1]
else:
    for i in range(0,len(minus)-1,2):
        answer+=minus[i]*minus[i+1]
    answer+=minus[-1]
print(answer)