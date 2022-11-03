t=int(input())
def make_c(a,b):
    num = len(a)
    c=[]
    ans=0
    for i in range(num):
        temp=a[i]
        start=0
        end=len(b)-1
        while start<=end:
            mid=(start+end)//2
            if b[mid]==temp:
                c.append(b[mid])
                mid=-1
                break
            elif b[mid]<temp:
                start=mid+1
            else:
                end=mid-1
        if mid==-1:
            continue
        elif temp<b[0]:
            c.append(b[0])
        elif temp>b[-1]:
            c.append(b[-1])
        elif abs(temp-b[start])>=abs(temp-b[end]):
            c.append(b[end])
        else:
            c.append(b[start])
    for i in range(num):
        ans+=c[i]
    return ans
answer=[]
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b=sorted(b)
    answer.append(make_c(a,b))
for i in range(t):
    print(answer[i])