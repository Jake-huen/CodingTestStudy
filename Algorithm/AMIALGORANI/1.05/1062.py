# from itertools import combinations
# n, k = map(int, input().split())
# if k < 5:
#     print(0)
# else:
#     k -= 5
#     alreadyLearned = {'a', 'n', 't', 'i', 'c'}
#     input_chars = []
#     alpha = {ky: v for v, ky in enumerate(
#         (set(map(chr, range(ord('a'), ord('z')+1))) - alreadyLearned))} # 이미 배운것은 뺴줌
#     cnt = 0
#     for _ in range(n):
#         tmp = 0
#         for c in set(input())-alreadyLearned:
#             tmp = tmp | (1 << alpha[c])
#         input_chars.append(tmp)
#     power_by_2 = (2**i for i in range(21))
#     for comb in combinations(power_by_2, k):
#         test = sum(comb)
#
#         ct = 0
#         for cb in input_chars:
#             if test & cb == cb:
#                 ct += 1
#
#         cnt = max(cnt, ct)
#     print(cnt)



import sys

input = sys.stdin.readline
from itertools import combinations


def antarctica(letters, toLearnList):
    # print(letters) [['r'], ['h', 'o', 'e', 'l'], ['r']]
    # print(toLearnList) ['e', 'h', 'o', 'r', 'l']
    if len(toLearnList)<k-5:
        print(len(letters))
    else:
        checks = list(combinations(toLearnList, k - 5))
        # print(checks) # [('o',), ('l',), ('h',), ('e',), ('r',)]
        answer = []
        for check in checks:
            ans = len(letters) # 처음엔 다 배울 수 있다고 가정하고 못배우는 걸 뺴는 방법으로
            check = list(check) # 필요한지 잘 모르겠음
            for letter in letters:
                if len(letter) > k - 5:  # 배워야 되는 숫자가 더 많음
                    ans -= 1
                    continue
                elif len(letter) == 0:  # 이미 다 배움
                    continue
                else:
                    for i in range(len(letter)):
                        if letter[i] in check:  # 조합으로 k-5만큼 선택한 배열 안에 있는 경우
                            continue  # 계속 진행
                        else:
                            ans -= 1  # 없을 경우 이 단어는 이 조합으로는 일단 만들 수 없다
                            break
            answer.append(ans)
        print(max(answer))


n, k = map(int, input().split())
alreadyLearned = {'a', 'c', 'i', 'n', 't'} # 무조건 a,c,i,n,t는 배워야 함. 최소 5개
letters = []  # 가르치는 단어들
toLearnList = set()  # 배워야하는 글자들
for i in range(n):
    letter = set(list(input())[4:-5]) - alreadyLearned  # 입력받은 단어를 앞뒤 다 짜르고 이미 배운거 빼기
    toLearnList.update(letter) # 배워야하는 곳에 추가하기
    letters.append(list(letter))
if k < 5:
    print(0)  # 아무것도 배울 수 없다.
else:
    antarctica(letters, list(toLearnList))
