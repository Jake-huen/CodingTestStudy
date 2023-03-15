def tentotwo(number, ans):  # 십진수-> 이진수
    if number == 0:
        return ans
    if number % 2 == 0:
        return tentotwo(number // 2, "0" + ans)
    elif number % 2 == 1:
        return tentotwo(number // 2, "1" + ans)
def adjustnumber(number):
    temp = 0
    for i in range(51):
        temp = 2**i-1
        if temp>=len(number):
            break
    return '0'*(temp-len(number))+number
def check(number,parent):
    if parent == '0': #만약에 루트 노드가 0이면 모든 child node는 0이어야 한다.
        for child in number:
            if child != '0':
                return False
    if len(number)==1: # 하나 밖에 없을때는 무조건 통과
        return True
    center = len(number)//2
    return check(number[:center],number[center]) and check(number[center+1:],number[len(number)-center-1])

def solution(numbers):
    answer = []
    for number in numbers:
        temp = tentotwo(number, "")
        temp = adjustnumber(temp)
        if check(temp,temp[len(temp)//2]):
            answer.append(1)
        else:
            answer.append(0)
    return answer