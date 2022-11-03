# 전투력 <=10000 : WEAK
# <=100000 : NORMAL
# <=1000000 : STRONG

n,m = map(int,input().split())
chingho=[]
power=[]
character=[]
for i in range(n):
    x,y = input().split()
    y = int(y)
    chingho.append(x)
    power.append(y)

# print(tmp[0])
print(chingho)
print(power)
for i in range(m):
    tmp = int(input())
    start =0
    end = len(power)-1
    while start<=end:
        mid=(start+end)//2
        if tmp>power[mid]:
            mid=start+1
        else:
            end=mid-1
    character.append((start,end))
for i in character:
    print(i)
