import sys
input = sys.stdin.readline
T = int(input())
letterlist = []
answers = []
for i in range(T):
    letter = list(input())
    letterlist.append(letter[:-1])
for letter in letterlist:
    left = 0
    right = len(letter) - 1
    answer = 2
    while True:
        if letter[left] == letter[right]:
            letter.pop(right)
            letter.pop(left)
            right = len(letter) - 1
            if len(letter) == 0 or len(letter) == 1:
                answer = 0
                break
        elif letter[left] != letter[right]: # 다른 경우
            temp1 = letter[left + 1:right + 1]
            if temp1[:] == temp1[::-1]:
                answer = 1
                break
            else:
                temp2 = letter[left:right]
                if temp2[:] == temp2[::-1]:
                    answer = 1
                break
    answers.append(answer)
for answer in answers:
    print(answer)