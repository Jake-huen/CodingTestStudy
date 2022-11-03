n,h,w = map(int,input().split())
bungin=[]
for i in range(h):
    bungin.append(list(input().split()))
# print(bungin[0][0][3])
# print(bungin)
answer=['?']*n
for i in range(n):
    for j in range(i*w,i*w+w):
        for k in range(h):
            if bungin[k][0][j]!='?':
                answer[i]=bungin[k][0][j]
            else:
                continue
for i in range(n):
    print(answer[i],end='')