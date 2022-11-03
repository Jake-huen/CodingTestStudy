n = int(input())
def jari(num):
    sum=0
    k=num
    while True:
        if num>=100000:
            sum+=num//100000
            num=num%100000
        elif num>=10000:
            sum+=num//10000
            num=num%10000
        elif num>=1000:
            sum+=num//1000
            num=num%1000
        elif num>=100:
            sum+=num//100
            num=num%100
        elif num>=10:
            sum+=num//10
            num=num%10
        else:
            sum+=num
            break
    return k+sum
answer=1000000
for i in range(n+1):
    if jari(i) == n:
        answer=min(answer,i)
if answer==1000000:
    print(0)
else:print(answer)