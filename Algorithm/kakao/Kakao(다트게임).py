# 다트 세 차례 던져 그 점수의 합계로 실력을 겨룬다
# 한번에 0~10
import math
def solution(dartResult):
    answer = 0
    split_index=[]
    for i in range(len(dartResult)):
        print(dartResult[i])
        if dartResult[i]>='0' and dartResult[i]<='10':
            split_index.append(i)
    print(split_index)
    one = dartResult[split_index[0]:split_index[1]]
    two = dartResult[split_index[1]:split_index[2]]
    three = dartResult[split_index[2]:len(dartResult)]
    for i in [one,two,three]:
        temp=0
        if i[1]=='S':
            temp+=math.pow(int(i[0],1))
        elif i[1]=='S':
            temp+=math.pow(int(i[0],2))
        elif i[1]=='S':
            temp+=math.pow(int(i[0],3))
        print(i)
    return answer
solution('1S2D*3T')