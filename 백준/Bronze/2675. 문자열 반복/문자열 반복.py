t = int(input())
def make_new(time, word):
    ans=""
    for i in range(len(word)):
        ans+=(word[i]*time)
    return ans
answers=[]
for i in range(t):
    x= list(input())
    #print(x[0],x[1:])
    answers.append(make_new(int(x[0]),list(x[2:])))
for answer in answers:
    print(answer)


