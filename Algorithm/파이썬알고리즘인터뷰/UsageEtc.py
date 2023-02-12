# 리스트 컴프리헨션
import collections

# 만약에 배열을 곱하기 2한 값을 리턴 받으려면?
first = list(map(lambda x: x * 2, [1, 2, 3]))
# print(first)
second = [n * 2 for n in range(10) if n % 3 == 0]  # [0,6,12,18]
# print(second)
dictionary_ex = {}
original = {"name": "김태헌", "email": "taehuen7757"}
for key, value in original.items():
    dictionary_ex[key] = value
# print(dictionary_ex)
dictionary_ex = {key: value for key, value in original.items()}
# print(dictionary_ex)


# 제너레이터
# yield 구문을 이용해서 제너레이터를 리턴할 수 있다
# return은 함수 자체를 종료하지만 yield는 실행 중이던 값을 내보낸다는 뜻

def get_natural_number():
    n = 0
    while True:
        n+=1
        yield n
g = get_natural_number()
#for _ in range(100):
    # print(next(g))
a = range(10000)
b = [i for i in range(10000)]
# print(a)
# print(b)

# enumerate : 열거하다
a = [1,2,3,4,5]
# for key,value in enumerate(a):
#     print(key, value)
a = ['a1','b2','c3']
# for key,value in enumerate(a):
#     print(key,value)

# 나눗셈
#print(5/3)
#print(5//3)
#print(divmod(5,3))

# print
a = [1,2,3,4,5]
#print(''.join(str(a)))


# 딕셔너리
a = dict()
a = {'name':'김태헌', 'email':'taehuen7757@gmail.com'}
# for k,v in a.items():
#     print(k,v)
del a['name']
# print(a)

# 딕셔너리 모듈
# defaultdict
a = collections.defaultdict()
a['A'] = 5
a['B'] = 3
# print(a)

# Counter : 아이템의 개수를 계산해서 dictionary로 리턴
a = [1,2,3,4,5,6,6]
b = collections.Counter(a)
# print(b)
# print(b.most_common(1))

# OrderedDict
a = {'name':'김태헌', 'email':'taehuen7757@gmail.com'}
b = collections.OrderedDict(a)
print(b)