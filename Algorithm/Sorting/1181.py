n = int(input())
datas=[]
for _ in range(n):
    word = input()
    word_c = len(word)
    datas.append((word,word_c))
#중복 값 제거
datas=set(datas)
datas=list(set(datas))

datas.sort(key=lambda word:(word[1],word[0]))

for i in range(len(datas)):
    print(datas[i][0])







