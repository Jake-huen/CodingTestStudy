def flip(some_list):
    if len(some_list)==0 or len(some_list)==1:
        return some_list
    return some_list[-1:]+flip(some_list[:-1])

some_list=[1,2,3]
print(some_list[-1])

