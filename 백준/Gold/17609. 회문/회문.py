import sys

input = sys.stdin.readline

T = int(input())
letterlist = []


def palindrom(letter):
    left = 0
    right = len(letter) - 1
    while left < right:
        if letter[left] == letter[right]:
            left += 1
            right -= 1
        elif letter[left] != letter[right]:  # 다른 경우
            if left < right - 1:
                temp = letter[:right] + letter[right + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left + 1 < right:
                temp = letter[:left] + letter[left + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0


for i in range(T):
    letter = list(input())[:-1]
    print(palindrom(letter))
