import sys
input = sys.stdin.readline

n,k = map(int,input().split())
products = list(map(int,input().split()))
multitab = [0]*(n)
idx =0
answer=0
for product in products:
    if product in multitab: #현재 꼽혀있음
        idx+=1
        continue
    if 0 in multitab: # 빈 공간 있을때
        multitab[multitab.index(0)] = product
        idx+=1
    else: # 빈 공간 없을때
        later=0 # 뽑아야 될 때 뒤에 있는거 뽑기 위함
        temp=0
        for i in multitab:
            if i not in products[idx:]: # 꼽혀있는 것 중에 더 이상 사용 안되는 것 뽑기
                temp=i
                break
            elif products[idx:].index(i) > later: # 더 나중에 사용되는 거 뽑기
                temp = i
                later = products[idx:].index(i)
        idx+=1
        multitab[multitab.index(temp)] = product
        answer+=1
print(answer)
