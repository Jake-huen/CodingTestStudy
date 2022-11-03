n = int(input())

result=[0]*n

answer = 0

datas = list(map(int,input().split()))

datas.sort()

result[0]=datas[0]
for i in range(1,len(datas)):
    result[i]=result[i-1]+datas[i]

for i in range(len(result)):
    answer+=result[i]

print(answer)