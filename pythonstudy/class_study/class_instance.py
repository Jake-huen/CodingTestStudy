class User:
    #pass#아무 내용이 없다는 뜻
    def say_hello(self):
        #인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    def login(self,my_email,my_password):
        #로그인 메소드
        if(self.email == my_email and self.password==my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")
    def check_name(self,name):
        #파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name==name

user1 = User()
user2 = User()
user3 = User()

user1.name="김대위"
user1.email = "captain@codeit.kr"
user1.password="12345"

User.say_hello(user1)
user1.say_hello()#파라미터가 없는데 왜 에러가 나지 않았을까
#인스턴스의 메소드를 호출하면 user1이 say_hello 첫번째 파라미터로 자동호출됨

#user1.login(user1,"captain@codeit.kr","12345") ->오류남
user1.login("captain@codeit.kr","12345")

#파이썬에서는 인스턴스의 첫번째 메소드를 self로 쓰라고 권장한다.
#인스턴스 메소드의 첫번째 파라미터의 이름은 꼭! self로 쓰기

print(user1.check_name("김대위"))
"""
#인스턴스 변수 정의하기
인스턴스 이름.속성이름(인스턴스 변수) = "속성에 넣을것"
인스턴스가 개인적으로 갖고 있는 것을 인스턴스 변수 라고 한다.(name,email,password)
속성 -> 변수
행동 -> 함수(메소드)
메소드의 종류
1.인스턴스 메소드 2.클래스 메소드 3.정적 메소드
1.인스턴스 메소드 : 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메소드
"""
