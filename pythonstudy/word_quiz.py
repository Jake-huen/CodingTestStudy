import random
ko = []
en = []
with open('vocabulary.txt','r',encoding='UTF-8') as f:
    for line in f:
        data=line.strip().split(": ")
        ko.append(data[1])
        en.append(data[0])
while True:
    i=random.randint(0,len(ko)-1)
    answer=input("{}: ".format(ko[i]))
    if answer=='q':
        break
    if answer==en[i]:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 {}입니다.".format(en[i]))