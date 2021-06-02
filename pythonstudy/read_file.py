with open('chicken.txt', 'r',encoding='UTF-8') as f:
    # for line in f:
    #     print(line)#한줄씩 띄엄띄엄 나옴
    for line in f:
        print(line.strip())