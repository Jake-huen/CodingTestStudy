def solution(balls, share):
    answer = 1
    for i in range(1,balls+1):
        answer*=i
    temp1=1
    for i in range(1,share+1):
        temp1*=i
    temp2=1
    for i in range(1,balls-share+1):
        temp2*=i
    answer = answer/(temp1*temp2)
    return answer