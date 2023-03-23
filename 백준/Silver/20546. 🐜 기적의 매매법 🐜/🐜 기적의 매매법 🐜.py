money = int(input())
prices = list(map(int, input().split()))


def jh(money):
    stocks = 0
    for price in prices:
        if money >= price:
            cnt = money // price
            money -= (price * cnt)
            stocks += cnt
    return money + stocks * prices[-1]


def sm(money):
    stocks = 0  # 남은 주식
    asc_count = 0
    desc_count = 0
    for idx, price in enumerate(prices):
        if idx > 1:
            if price > prices[idx - 1]:  # 상승하는 경우
                if desc_count == 0:
                    asc_count += 1
                    if asc_count >= 3:  # 3일 연속 상승하면 팔아야 함.
                        money += (price * stocks)
                        stocks = 0

                else:
                    asc_count = 1
                    desc_count = 0
            elif price < prices[idx - 1]:  # 하락하는 경우
                if asc_count == 0:
                    desc_count += 1
                    if desc_count >= 3:  # 3일 연속 하락했으면 사야 함.
                        cnt = money // price
                        money -= (price * cnt)
                        stocks += cnt
                else:
                    asc_count = 0
                    desc_count = 1
            else:
                asc_count = 0
                desc_count = 0
    return money + stocks * prices[-1]


a = jh(money)
b = sm(money)
if a > b:
    print("BNP")
elif a == b:
    print("SAMESAME")
else:
    print("TIMING")


