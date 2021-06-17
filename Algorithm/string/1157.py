from collections import Counter
word = input()
word = word.lower()
if len(word)>1 and Counter(word).most_common(2)[1][1]==Counter(word).most_common(2)[0][1]:
    print('?')
else:
    temp=Counter(word).most_common()[0][0]
    print(temp.upper())