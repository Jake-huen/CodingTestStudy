sik = input().split('-')
number=[]
for i in sik:
    result = 0
    s=i.split('+')
    for j in s:
        result+=int(j)
    number.append(result)
ans=0
for i in range(len(number)):
    if i==0:
        ans+=number[i]
    else:
        ans-=number[i]
print(ans)


