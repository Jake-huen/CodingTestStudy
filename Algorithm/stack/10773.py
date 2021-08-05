k = int(input())
number=[]
result=0
for i in range(k):
    x = int(input())
    if x==0:
        number.pop()
    else:
        number.append(x)
for i in range(len(number)):
    result+=number[i]

print(result)