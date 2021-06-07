class User:
    def __init__(self,name,email,pw):
        self.name=name
        self.email=email
        self.pw=pw

    def say_hello(self):
        print("안녕! 나는 {}이야".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: *****".format(self.name,self.email)
    """
    double underscore dunder메소드 dunder에스티알
    dunder에스티알 메소드 호출되는 경우:
    print함수 호출할 때 자동으로 호출됨
    """

user1=User("김태헌","tae77777@naver.com","rlaxogjs8312@")
user2=User("너굴너굴너굴맨","namu0916","kth8312@")

print(user1)
print(user2)