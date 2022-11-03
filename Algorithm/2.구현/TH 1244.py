def onezero(num):
    if switch[num] == 0:
        switch[num]=1
    elif switch[num]==1:
        switch[num]=0
    return


n = int(input())
switch = [-1] + list(map(int,input().split()))
cnt = int(input())
for i in range(cnt):
    student,number = map(int,input().split())
    if student == 1:  # 남학생인 경우
        for i in range(len(switch)):
            if i % number == 0:
                onezero(i)
    elif student==2:
        temp = min(len(switch)-number-1,number-1)
        # print(f"temp = {temp}")
        for i in range(temp+1):
            if switch[number+i]==switch[number-i]:
                if i==0:
                    onezero(number)
                else:
                    onezero(number+i)
                    onezero(number-i)
            else:
                break
    # print(switch)
for i in range(1,len(switch)):
    print(switch[i],end=' ')
    if i % 20 == 0 :
        print()
