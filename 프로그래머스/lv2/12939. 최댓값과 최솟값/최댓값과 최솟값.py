def solution(s):
    temp = list(map(int,s.split()))
    answer = ''
    answer+=str(min(temp))
    answer+=' '
    answer+=str(max(temp))
    return answer
