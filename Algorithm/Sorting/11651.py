n = int(input())

answer=[]

for i in range(n):
    x,y = map(int,input().split())
    answer.append((x,y))

answer = sorted(answer,key=lambda x:(x[1],x[0]))

for i in range(n):
    print(str(answer[i][0])+' '+str(answer[i][1]))


#출력초과?
