n = int(input())
cards=[]
result=0
for i in range(n):
    cards.append(int(input()))
cards.sort()
for i in range(n-1):
    temp = cards[0]
    del cards[0]
    cards.sort()
    temp = temp+cards[0]
    result+=temp
    del cards[0]
    cards.append(temp)
print(result)
