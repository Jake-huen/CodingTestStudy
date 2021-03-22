n = int(input())

datas=[]
for _ in range(n):
    datas.append(int(input()))

def first(datas):
    result=0
    for data in datas:
        result+=data
    return result//len(datas)

def second(datas):
    datas.sort()
    mid = (0+len(datas)-1)//2
    return datas[mid]

def third(datas):
    #dictionary 사용
    dictionary={}
    for data in datas:
        if data<0: data=-data+4000
        if dictionary.get(data) is None:
            dictionary[data]=1
        else:
            dictionary[data]+=1
    most = max(dictionary.values())
    max_list={}
    for key,value in dictionary.items():
        if value==most:
            max_list[key]=value
    if len(max_list)==1:
        if key>4000:key=-(key-4000)
        print(key)
    else:
        if key>4000:key=-(key-4000)
        for key,value in max_list.items():
            print(key,end=' ')




def fourth(datas):
    datas.sort()
    return datas[len(datas)-1]-datas[0]

print(first(datas))
print(second(datas))
print(third(datas))
print(fourth(datas))