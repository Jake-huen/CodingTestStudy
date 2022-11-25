n = int(input())
# result = [0]*(n+1) # 0이면 상근이가 이기고, 1이면 창영이가 이기는 거
if n==1:
    print('SK')
    exit(0)
else:
    if n%7==0 or n%7==2:
        print('CY')
    else:
        print('SK')

















    # if n>=5:
    #     for i in range(5,n+1):
    #         one = result[i-1]
    #         two = result[i-3]
    #         three = result[i-4]
    #         if one==1 or two==1 or three==1:
    #             result[i]=0
    #         else:
    #             result[i]=1
    # if result[n]==0:
    #     print('SK')
    # else:
    #     print('CY')