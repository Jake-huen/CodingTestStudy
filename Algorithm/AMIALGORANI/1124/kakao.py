from collections import defaultdict
from itertools import combinations


def make_gift_map(gifts):
    gift_count = defaultdict(lambda: defaultdict(int))

    for gift in gifts:
        giver, receiver = gift.split()
        gift_count[giver][receiver] += 1
    result = {}
    for giver, receivers in gift_count.items():
        result[giver] = [{receiver: count} for receiver, count in receivers.items()]
    return result


def get_give_and_take(friends, gift_map):
    gift_counts = {friend: [0, 0] for friend in friends}
    result = {friend: 0 for friend in friends}
    # print(gift_counts)
    for giver, receivers in gift_map.items():
        for receiver_info in receivers:
            receiver, count = next(iter(receiver_info.items()))
            # print(giver, receiver, count)
            gift_counts[giver][0] += count  # 선물 준사람꺼 업데이트
            gift_counts[receiver][1] += count  # 선물 받은사람꺼 업데이트
    for friend in gift_counts.keys():
        result[friend] = gift_counts[friend][0] - gift_counts[friend][1]
    # print(gift_counts)
    return result


def calculate_next_month(friends, present_idx, gift_map):
    next_month_gifts = {friend: 0 for friend in friends}
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            one = friends[i]
            two = friends[j]
            one_give = 0
            two_give = 0
            print(one, two)
            if one in gift_map:  # 주고받은 기록이 있을때
                for item in gift_map[one]:
                    one_give += item.get(two,0)

            if two in gift_map:
                for item in gift_map[two]:
                    two_give += item.get(one,0)
            print(one, one_give)
            print(two, two_give)
            print()
            if one_give > two_give:
                next_month_gifts[one] += 1
                print("여기1", one, two, one_give, two_give)
            elif one_give < two_give:
                next_month_gifts[two] += 1
                print("여기2", one, two, one_give, two_give)
            elif one_give == two_give:
                if present_idx[one] > present_idx[two]:
                    next_month_gifts[one] += 1
                    print("여기3", one, two, one_give, two_give)
                elif present_idx[one] < present_idx[two]:
                    next_month_gifts[two] += 1
                    print("여기4", one, two, one_give, two_give)
    print(present_idx)
    print(gift_map)
    return next_month_gifts


def solution(friends, gifts):
    answer = 0
    gift_map = make_gift_map(gifts)
    # print(gift_map)
    present_idx = get_give_and_take(friends, gift_map)
    # print(present_idx)
    result = calculate_next_month(friends, present_idx, gift_map)
    print(result)
    for friend in result:
        answer = max(answer, result[friend])
    return answer


solution(["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
# solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])
