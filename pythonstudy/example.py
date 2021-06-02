import datetime
#datetime 값 생성
yesterday=datetime.datetime(2021,5,28)
print(yesterday)#2021-05-29 00:00:00

#오늘 날짜
today = datetime.datetime.now()
print(today)

#timedelta - 두 datetime 값 사이의 기간을 알고 싶을때
today = datetime.datetime.now()
pi_day=datetime.datetime(2020,3,14,13,6,15)
print(today-pi_day)#441 days, 7:34:40.480029
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)
print(today + my_timedelta)

#datetime 해부하기
today = datetime.datetime.now()
print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

#datetime 포맷팅
today = datetime.datetime.now()
print(today)
print(today.strftime("%A, %B %dth %Y"))