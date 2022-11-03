menu = 0
number = 0
price =0
total =0

print("="*50)
print("[1]팝콘:5000원 [2]나쵸:4000원 [3]핫도그:3500원 [4]음료:2000원")
print("주문을 끝내려면 [0]을 입력하세요.")
print("="*50)

while True:
    menu = int(input("선택메뉴: "))
    if menu==0:
        break
    number = int(input("주문 수량: "))

print("*" * 50)
print("금액합계: {}".format(total))