n = int(input())
def temp(word):
    new = []
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i+1] not in new:
                new.append(word[i])
            else:
                return False
    return True
answer=0
for i in range(n):
    word = input()
    if temp(word):
        # print(word)
        answer+=1
print(answer)