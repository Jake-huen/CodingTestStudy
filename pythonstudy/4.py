import random
score = 0
for i in range(3):
    a,b = random.sample(range(1,100),2)
    user = int(input(str(a)+' + '+str(b)+'='))

    if user==a+b:
        score+=5
print("총 득점:{}점".format(score))
