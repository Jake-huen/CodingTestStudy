from random import randint


def generate_numbers(n):
    list=[]
    for i in range(n):
        temp = randint(1,45)
        if temp not in list:
            list.append(temp)
    return list

def draw_winning_numbers():
    list = generate_numbers(6)
    list.sort()
    while True:
        bonus_number = randint(1,45)
        if bonus_number not in list:
            list.append(bonus_number)
            break
    return list

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    temp = count_matching_numbers(numbers, winning_numbers[:-1])
    bonus=0
    if winning_numbers[-1] in numbers:
        bonus=1
    if temp == 6:
        return 1000000000
    elif temp == 5 and bonus == 1:
        return 50000000
    elif temp == 5:
        return 1000000
    elif temp == 4:
        return 50000
    else:
        return 5000