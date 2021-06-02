from random import randint
print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
answer=[]
for i in range(3):
    answer.append(randint(0,9))
print(answer)
print()
chance=0
while True:
    i = 1
    list = []
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    while i<4:
        x=int(input("{}번째 숫자를 입력하세요: ".format(i)))
        if x in list:
            print("중복되는 숫자 입니다. 다시 입력하세요.")
        elif x<0 or x>9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            list.append(x)
            i+=1
    print(list)
    strike=0
    ball=0
    for i in range(len(answer)):
        for j in range(len(list)):
            if answer[i]==list[j]:
                if i==j:
                    strike+=1
                else:
                    ball+=1
    print("{}S {}B".format(strike,ball))
    chance+=1
    if strike==3 and ball==0:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(chance))
        break

