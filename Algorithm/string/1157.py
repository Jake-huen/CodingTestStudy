from collections import Counter
word = input()
word = word.lower()
print(len(Counter(word).most_common(1)))
if len(Counter(word).most_common(1))==2:
    print('?')
else:
    print(Counter(word).most_common(1)[0][0].upper())