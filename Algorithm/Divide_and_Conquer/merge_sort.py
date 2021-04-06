def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    # 코드를 작성하세요.
    merged_list=[]
    index1=0
    index2=0
    while index1<len(list1) and index2<len(list2):
        if list1[index1]<list2[index2]:
            merged_list.append(list1[index1])
            index1+=1
        else:
            merged_list.append(list2[index2])
            index2+=1
    merged_list=merged_list+list1[index1:]+list2[index2:]
    return merged_list
# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    list1 = []
    list2 = []
    mid = len(my_list)//2
    list1.append(my_list[:mid])
    list2.append(my_list[mid:])
    return merge(merge_sort(list1),merge_sort(list2))
# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

