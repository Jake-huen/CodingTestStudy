n = int(input())
letters = []
for _ in range(n):
    letters.append(list(input()))
alphabet = [0] * 26
for letter in letters:
    for j in range(len(letter) - 1, -1, -1):
        temp = ord(letter[j]) - 65  # 해당 알파벳 배열 index
        alphabetPriority = 10 ** (len(letter)-j)  # 우선순위
        alphabet[temp] += alphabetPriority
alphabet_number = []
for i in range(26):
    if alphabet[i] != 0:
        alphabet_number.append([chr(i + 65), alphabet[i]])
# print(alphabet_number)
alphabet_number.sort(key=lambda x: x[1], reverse=True)
temp = 9
for i in range(len(alphabet_number)):
    alphabet_number[i][1] = temp
    temp -= 1
# print(alphabet_number)
calculate=[]
for letter in letters:
    for i in range(len(letter)):
        for j in range(len(alphabet_number)):
            if letter[i] == alphabet_number[j][0]:
                letter[i] = alphabet_number[j][1]
    temp=0
    for i in range(len(letter)):
        temp += letter[i]*(pow(10,len(letter)-1-i))
    calculate.append(temp)
answer=0
for i in range(len(calculate)):
    answer+=calculate[i]
print(answer)
# print(ord('A')-65)
# print(ord('Z')-65)
