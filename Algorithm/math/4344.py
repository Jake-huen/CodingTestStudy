c = int(input())
high=[]
for j in range(c):
    student=list(map(int,input().split()))
    stu=len(student)-1
    n=student[0]
    student_average=0
    for i in range(1,len(student)):
        student_average+=student[i]
    student_average=student_average/stu
    high_average=0
    for i in range(1,len(student)):
        if student[i]>student_average:
            high_average+=1
    high.append(high_average / stu * 100)
for i in range(c):
    print("{:.3f}%".format(high[i],3))
