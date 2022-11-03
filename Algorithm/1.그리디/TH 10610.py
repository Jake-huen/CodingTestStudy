N = list(input())
# 30 = 2 X 3 X 5
answer=True
check3 =0
for i in range(len(N)):
    check3+=int(N[i])
if check3%3!=0:
    answer=False
check5=False
for i in range(len(N)):
    if int(N[i])==0:
        check5=True
        break
    else:
        continue
if check5==False:
    answer=False
if(answer):
    for i in range(len(N)):
        N[i]=int(N[i])
    N.sort(reverse=True)
    for i in range(len(N)):
        print(N[i],end='')
else:
    print(-1)
