"""
서로 공유하는 값:class변수
같은 클래스의 instance들이 공유하는 값

클래스 변수가 유저 인스턴스 개수를 정확히 나타내도록 하려면?
user instance가 생성될때마다 count를 늘리면 된다. ->__init__에서 늘리면 된다.
한 클래스의 모든 인스턴스가 공유하는 속성 --->클래스 변수
클래스 변수의 값 읽는 법?
1.클래스 이름.클래스 변수 이름
2.인스턴스 이름.클래스 변수 이름
같은 이름의 클래스 변수 VS 같은 이름의 인스턴스 변수(인스턴스 변수WIN)
클래스 변수의 값 설정하기
-->그러므로 클래스 변수에 값을 설정할 때는 클래스 이름으로만!
"""
class User:
    count = 0
    def __init__(self,name,email,pw):
        self.name=name
        self.email=email
        self.pw=pw

        User.count+=1
