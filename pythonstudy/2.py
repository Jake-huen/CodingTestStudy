while True:
    num = int(input('수 입력(종료는 0을 입력하세요):'))
    if num==0:
        break
    else:
        count=0
        a = num//10
        b = num%10
        if a%3==0:
            count+=1
        if b%3==0:
            count+=1
        for i in range(count):
            print("clap!",end='')
    print()
print("게임종료")