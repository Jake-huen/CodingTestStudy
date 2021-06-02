import random

# 코드를 작성하세요.
chance=0
answer = random.randint(1,20)
while chance<4:
    x=int(input('기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: '.format(4-chance)))
    chance += 1
    if x==answer:
        print('축하합니다. {}번만에 숫자를 맞히셨습니다.'.format(chance))
        break
    elif x<answer:
        print('UP')
    elif x>answer:
        print('Down')
if chance==4:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))