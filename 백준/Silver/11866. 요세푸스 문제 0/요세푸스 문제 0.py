n,k = map(int,input().split())
round_table=[]
for i in range(1,n+1):
    round_table.append(i)
answers=[]
current = 0
while len(round_table)!=0:
    index = current+(k-1) # 빼내야 되는 사람의 index
    if index >= len(round_table):
        while index >= len(round_table):
            index = index % len(round_table)
        answer = round_table.pop(index)
    else:
        answer = round_table.pop(index)
    current = index
    answers.append(answer)
if len(answers)==1:
    print(f"<{answers[0]}>")
else:
    for (idx,val) in enumerate(answers):
        if idx==0:
            print("<",end="")
            print(val,end=", ")
        elif idx==len(answers)-1:
            print(val,end=">")
        else:
            print(val, end = ", ")

