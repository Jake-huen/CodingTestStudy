from itertools import product
def buy(discount_case, limit, emoticons):
    total = 0
    for idx,discount in enumerate(discount_case):
        if discount>=limit:
            total+= emoticons[idx]*(100-discount)//100
    return total

def solution(users, emoticons):
    answer = []
    discounts = [10,20,30,40]        
    emoticons_count = len(emoticons)
    discount_cases = list(product(discounts,repeat = emoticons_count))
    result = []
    for discount_case in discount_cases:
        emoticon_plus = 0
        sales=0
        for user in users:
            buy_price = buy(discount_case,user[0],emoticons)
            if buy_price >= user[1]:
                emoticon_plus+=1
            else:
                sales+=buy_price
        result.append([emoticon_plus, sales])
    # print(sorted(result,reverse=True))
    answer = sorted(result,reverse=True)[0]
    return answer