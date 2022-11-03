n = input()

def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]
def temp(n):
    if len(n)==1:
        answer = 0
        if int(n)%2==1:
            answer+=1
        return answer
    elif len(n)==2:
        answer = 0
        if int(n[0])%2==1:
            answer+=1
        if int(n[1])%2==1:
            answer+=1
        if (int(n[0])+int(n[1]))%2==1:
            answer+=1
        return answer
    elif len(n==3):
        answer = 0
        if int(n[0])%2==1:
            answer+=1
        if int(n[1])%2==1:
            answer+=1
        if int(n[2])%2==1:
            answer+=1
        if (int(n[0]) + int(n[1])+int(n[2])) % 2 == 1:
            answer+=1
        return answer
    else:
        answer=0
        result_array = list_chuck(n,3)
        for i in range(len(result_array)):
            answer+=temp(result_array[i])
        return answer


