n = int(input())
meeting=[]
for i in range(n):
    start,end= map(int,input().split())
    meeting.append((start,end))

#시작 시간 기준으로 정렬
meeting=sorted(meeting,key=lambda x:x[0])
#종료 시간 기준으로 정렬
meeting=sorted(meeting,key=lambda x:x[1])
start_time=0
result=0
for time in meeting:
    if time[0]>=start_time:
        start_time=time[1]
        result+=1

print(result)
