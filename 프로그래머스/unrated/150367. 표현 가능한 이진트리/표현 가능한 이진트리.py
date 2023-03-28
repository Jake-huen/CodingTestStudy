

def solution(numbers):
    answer = []
    def tentotwo(number):
        ans=''
        while number!=0:
            if number%2==0:
                ans = '0'+ans
                number = number//2
            elif number%2==1:
                ans = '1'+ans
                number = number//2
        return ans
    def fillnumber(number):
        for i in range(50):
            temp = 2**i-1
            if temp>=len(number):
                return '0'*(temp-len(number))+number
    def check(number):
        if len(number)==1:
            return True
        mid = len(number)//2
        if number[mid]=='0':
            for i in range(len(number)):
                if number[i]=='1':
                    return False
            return True
        elif number[mid]=='1':
            first = number[0:mid]
            second = number[mid+1:]
            return check(first) and check(second)
    for number in numbers:
        number = tentotwo(number)
        number = fillnumber(number)
        if check(number):
            answer.append(1)
        else:
            answer.append(0)
    return answer