#from 모듈의 이름 import 불러올 변수/함수/클래스 이름
#from calculator import sum, difference, product, square
"""
uniform도 random 모듈에 있는 함수인데요,
두 수 사이의 랜덤한 소수(난수)를 리턴하는 함수입니다.

다음을 실행하면 0과 1사이의 소수 중 랜덤으로 한 가지 수가 출력됩니다.

"""
from random import uniform
# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴한다.
x = uniform(0, 1)
print(x)