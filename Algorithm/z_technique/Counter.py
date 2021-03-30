#데이터의 개수를 셀 때 유용한 collections 모듈의 Counter 클래스 사용법
def countLetter(word):
    counter={}
    for letter in word:
        if letter not in counter:
            counter[letter]=0
        counter[letter]+=1
    return counter
#데이터의 개수를 셀 때 사전이 많이 사용된다.
#이것을 collection모듈의 counter클래스로 바꿀 수 있다.
from collections import Counter
Counter('hello world')

#collections.Counter 기본 사용법
#collections모듈의 Counter클래스는 파이썬의 기본 자료구조인 사전을 확장하고 있음

#주어진 단어에서 가장 많이 등장하는 알파벳과 그 갯수
from collections import Counter
def find_max(word):
    counter = Counter(word)
    max_count=-1
    for letter in counter:
        if counter[letter]>max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter,max_count
#이걸 더 간단하게 할 수 있음
Counter('hello world').most_common()# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(1) # [('l', 3)]
