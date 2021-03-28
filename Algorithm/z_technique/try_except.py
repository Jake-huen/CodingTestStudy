#파이썬 리스트 중복 요소 개수 찾기(카운팅) or 제거, 삭제하기 (try , except , count)

#1. 중복요소 카운팅하기
count={}
lists = ["a","a","b",'apple','w','wf']
for i in lists:
    try: count[i] += 1
    except: count[i]=1
print(count)

#결과값 : {'a': 2, 'b': 1, 'apple': 1, 'w': 1, 'wf': 1}

#for문을 통해 lists의 요소를 하나씩 꺼내어, count라는 이름의 딕셔너리에 넣는다.
#이때 count에 이미 존재하는 key값이라면, try문이 실행되며 value에 +1을 하게 된다.
#count에 없는 key값이라면 except가 실행되며 value는 그냥 1로 저장된다.

#2.중복요소 삭제, 제거하기
#set이용하기
arr = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
arr = set(arr) # "arr"라는 리스트의 데이터 타입을 set으로 바꾼다.
#set은 중복요소를 허용하지 않는 데이터형태이기 때문에, 중복요소들이 제거된다.
arr = list(arr)