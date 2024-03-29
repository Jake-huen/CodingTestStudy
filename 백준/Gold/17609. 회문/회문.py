import sys

input = sys.stdin.readline

T = int(input())
letterlist = []


def palindrom(letter):
    left = 0
    right = len(letter) - 1
    while True:
        if letter[left] == letter[right]:
            left += 1
            right -= 1
            if left >= right:
                break
        elif letter[left] != letter[right]:  # 다른 경우
            temp = letter[:right] + letter[right + 1:] # right를 제외시킴
            if temp[:] == temp[::-1]:
                return 1
            temp = letter[:left] + letter[left + 1:] # left를 제외시킴
            if temp[:] == temp[::-1]:
                return 1
            return 2
    return 0


for i in range(T):
    letter = list(input())[:-1]
    print(palindrom(letter))
