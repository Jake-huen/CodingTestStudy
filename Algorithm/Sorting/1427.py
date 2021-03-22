n= int(input())
data=[]
data = list(map(int,str(n)))
data.sort(reverse=True)
for i in data:
    print(i,end="")
