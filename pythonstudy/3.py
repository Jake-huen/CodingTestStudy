import random
std_score = []
count=[0,0,0,0,0]

std_score = random.sample(range(1,101),5)
print(std_score)

for i in std_score:
    if i>=90:
        count[0]+=1
    elif i>=80:
        count[1]+=1
    elif i>=70:
        count[2]+=1
    else:
        count[3]+=1
print('A학점:{},B학점:{},C학점:{},재수강:{}'.format(count[0],count[1],count[2],count[3]))
