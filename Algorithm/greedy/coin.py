def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    default_coin_list.sort(reverse=True)
    answer =0
    for coin in coin_list:
        if value>coin:
            answer+=value//coin
            value=value%coin
    return answer
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))