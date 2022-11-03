from random import randint
print("구구단 게임 시작!")

correct =0
wrong =0

while True:
    a = randint(2,9)
    b=randint(2,9)
    k=input('준비되면 엔터, 종료하려면 0 입력: ')
    if k=='0':
        break
    my =int(input('{}*{}='.format(a,b)))
    if my==a*b:
        correct+=1
        print('정답!',f'성공:{correct}점, 실패:{wrong}점')
    else:
        wrong+=1
        print("오답!",end='')
print('성공:{}점, 실패:{}점'.format(correct,wrong))