def print_hello():
    print("안녕하세요!")

def add_print_to(original):#데코레이터 함수
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

print_hello = add_print_to(print_hello)
print_hello()

#데코레이터 함수의 쓸모
#중복이 많을때
@add_print_to
def function1():
    #기존 함수1 내용

@add_print_to
def function2():
    #기존 함수2 내용

@add_print_to
def function3():
    #기존 함수3 내용

"""
@classmethod
def function():
    함수내용
기존 함수에 새로운 기능 추가
"""