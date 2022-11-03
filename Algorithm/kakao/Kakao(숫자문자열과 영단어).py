# def solution(s):
#     answer=''
#     i=0
#     while i<len(s):
#         if s[i]=='z':
#             answer+='0'
#             i+=4
#         elif s[i]=='o':
#             answer+='1'
#             i+=3
#         elif s[i]=='t':
#             if s[i+1]=='w':
#                 answer+='2'
#                 i+=3
#             elif s[i+1]=='h':
#                 answer+='3'
#                 i+=5
#         elif s[i]=='f':
#             if s[i+1]=='o':
#                 answer+='4'
#                 i+=4
#             elif s[i+1]=='i':
#                 answer+='5'
#                 i+=4
#         elif s[i]=='s':
#             if s[i+1]=='i':
#                 answer+='6'
#                 i+=3
#             elif s[i+1]=='e':
#                 answer+='7'
#                 i+=5
#         elif s[i]=='e':
#             answer+='8'
#             i+=5
#         elif s[i]=='n':
#             answer+='9'
#             i+=4
#         else:
#             answer+=s[i]
#             i+=1
#     return int(answer)

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("onefourzero4"))