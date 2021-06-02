def max_profit(stock_list):
    # 코드를 작성하세요.
    max_so_far=stock_list[0]-stock_list[1]
    max_check=max(stock_list[0],stock_list[1])
    for i in range(2,len(stock_list)):
        max_check=max(max_check,stock_list[i])
        print("max_check",i,max_check)
        max_so_far=max(max_so_far,max_check-stock_list[i])
        print("현재최대",max_so_far)
    return max_so_far

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))