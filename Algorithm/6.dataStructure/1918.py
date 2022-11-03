#후위 표기법
middle = input().split()

def change(temp):
    one=[]
    two=[]
    for i in range(len(temp)):
        if temp[i]=='*' | temp[i] =='/':
            one.append(temp[i])