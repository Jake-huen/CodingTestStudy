def merge(list1, list2):
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
    return merge(merge_sort(my_list[:len(my_list)//2]),merge_sort(my_list[len(my_list)//2:]))
# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))