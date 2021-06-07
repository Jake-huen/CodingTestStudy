class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
    #magic method, special method
    #특수 메소드, 특정 상황에서 자동으로 호출되는 메소드
    #init메소드 : 인스턴스가 생성될 때 자동으로 호출

user1 = User("Young", "young@codeit.kr", "123456")
#이 줄이 실행될 때 일어나는 일
#1.User 인스턴스 생성
#2.__init__메소드 자동 호출
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
