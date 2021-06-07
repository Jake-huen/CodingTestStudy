class User:
    count = 0
    def __init__(self,name,email,pw):
        self.name=name
        self.email=email
        self.pw=pw

        User.count+=1
    def say_hello(self):
        print("안녕! 나는 {}이야".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: *****".format(self.name,self.email)
    """
    인스턴스 변수의 값을 읽거나 설정하는 메소드 -> 인스턴스 메소드
    클래스 변수의 값을 읽거나 설정하는 메소드 -> 클래스 메소드
    
    클래스 메소드의 특별한 규칙:
    첫 번째 파라미터의 이름은 꼭! cls로 쓰기
    
    클래스 메소드는 같은 클래스로부터 만들어진 모든 인스턴스가 
    공통적으로 같은 처리를 할 때 사용할 메소드
     
    왜 클래스 메소드로 만들었을까?
    number_of_users가 인스턴스 변수를 사용하지 않기 때문에
    클래스 변수만 사용한다면 classmethod로 작성해야 한다.
    
    인스턴스 변수, 클래스 변수 둘 다 쓴다면 인스턴스 메소드를 사용한다.
    """
    #@classmethod -> 데코레이터
    #def number_of_users(cls):
    #    #cls.count // User.count
    #    print("총 유저 수는 {}".format(cls.count))

    def number_of_users(self):
        print("총 유저 수는 {}".format(User.count))

user1 = User("강영훈","yoon@codeit.kr","123456")
user2 = User("이윤수","tae888@codeit.kr","abcdef")

User.number_of_users(user1)
user1.number_of_users()