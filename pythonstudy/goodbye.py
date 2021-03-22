def binary_search(element, some_list):
    # 코드를 작성하세요.
    start = 0
    end = len(some_list)
    print(end)
    while start <= end:
        middle = (start+end)//2
        print(middle)
        if element == some_list[middle]:
            return middle
        elif element < some_list[middle]:
            end = middle-1
        elif element > some_list[middle]:
            start = middle+1
    return None
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))