# A:1 Z:26
n=list(input())
d=[0]*len(n)
#print(d)
if n[0]=='0':
    print(0)
else:
    d[0]=1
    for i in range(1,len(n)):
        temp = int(n[i-1])*10+int(n[i])
        if int(n[i])>0:
            d[i]+=d[i-1]
        if temp>=10 and temp<=26:
            if i==1:
                d[i]+=1
            else:
                d[i]+=d[i-2]
    print(d[len(n)-1]%1000000)