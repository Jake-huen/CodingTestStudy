from itertools import combinations

def beauty(one,two):
    check_one = len(one[0]) - len(one[2])
    check_two = len(two[0]) - len(two[2])
    if check_one == check_two: # 1번 통과
        if (len(one[0])+len(one[2]))==(len(two[0])+len(two[2])): # 2번 통과
            if (sum(one[0])+one[1]+sum(one[2]))==(sum(two[0])+two[1]+sum(two[2])): # 3번 통과
                if one[1]==0: # 짝수일때
                    one_temp = (''.join(str(s) for s in one[0])).join(str(s) for s in one[2])
                    two_temp = (''.join(str(s) for s in two[0])).join(str(s) for s in two[2])
                    if one_temp>two_temp:
                        return one
                    else:
                        return two
                else:
                    one_temp = (' '.join(str(s) for s in one[0])).join(str(one[1])).join(str(s) for s in one[2])
                    two_temp = (' '.join(str(s) for s in two[0])).join(str(two[1])).join(str(s) for s in two[2])
                    if one_temp > two_temp:
                        return one
                    else:
                        return two
            else:
                if sum(one)>sum(two):
                    return one
                else:
                    return two
        else:
            if len(one)>len(two):
                return one
            else:
                return two

    else:
        if check_one>check_two:
            return one
        else:
            return two


def siso(marbles):
    answers=[]
    if len(marbles)%2!=0:
        for i in range(len(marbles)):
            middle=marbles[i]
    else:
        cases=[]
        all_sum = sum(marbles)
        for j in range(1,len(marbles)//2+1):
            case = list(combinations(marbles, j))
            for i in range(len(case)):
                temp = sum(case[i])
                if temp==(all_sum-temp):
                    cases.append((list(case[i]),0,list(set(marbles)-set(case[i]))))
        return cases
def solution(marbles):
    answer=[]
    cases = siso(marbles)
    temp=cases[0]
    for i in range(1,len(cases)):
        temp = beauty(temp,cases[i])
    print(temp)
    return answer


# siso([1,2,3,4,5,8,10,13])
# beauty(([10, 13], 0, [1, 2, 3, 4, 5, 8]),([2, 8, 13], 0, [1, 3, 4, 5, 10]))
solution([3,9,7,5])