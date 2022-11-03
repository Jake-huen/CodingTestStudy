n = int(input())

data=[]
for _ in range(n):
    data.append(int(input()))

data.sort()
bigg=0
for i in range(n):
    imsy = data[i]*(n-i)
    if imsy>bigg:
        bigg=imsy
print(bigg)