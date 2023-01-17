import math
roomNumber = list(input())
sixNine = 0
number=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(roomNumber)):
    if roomNumber[i] == '6' or roomNumber[i] == '9':
        sixNine+=1
    else:
        number[int(roomNumber[i])]+=1
sixNine = round(sixNine/2+0.1)
temp = max(number)
print(max(temp,sixNine))
