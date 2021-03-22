def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    if start_index>end_index: return

    mid = (start_index+end_index)//2
    if some_list[mid]==element:
        return mid
    elif some_list[mid]<element:
        end_index=mid-1
    elif some_list[mid]>element:
        start_index=mid+1
    return binary_search(element,some_list,start_index,end_index)
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
