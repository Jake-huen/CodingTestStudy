testcase = int(input())
realanswers=[]
for _ in range(testcase):
    m = int(input())
    answers = [1]
    check = 1
    ans = []
    while check != m:
        new_answers = []
        for answer in answers:
            temp1 = str(answer) + "+" + str(check + 1)
            temp2 = str(answer) + "-" + str(check + 1)
            temp3 = str(answer) + " " + str(check + 1)
            new_answers.append(temp1)
            new_answers.append(temp2)
            new_answers.append(temp3)
        answers = new_answers
        check += 1
    for i, answer in enumerate(answers):
        if eval(answer.replace(" ", "")) == 0:
            ans.append(answer)
    ans.sort()
    realanswers.append(ans)
for realanswer in realanswers:
    for i in range(len(realanswer)):
        print(realanswer[i])
    print()
