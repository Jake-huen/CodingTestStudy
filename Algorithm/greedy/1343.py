"""
처음에 노가다식으로 하나씩 풀었음
replace 함수를 쓰면 greedy algorithm에도 잘 들어맞고(XXXX는 바로 AAAA로 바꾸어주고
XX는 다음에 만나면 바로 BB로 바꾸어주면 되기 때문)
replace 함수 기억하기
"""
# boards = input()
# temp=0
# answer=''
# check=0
# for i in range(len(boards)):
#     if boards[i]=='X':
#         temp+=1
#         if temp==4:
#             answer+='AAAA'
#             temp=0
#         if temp==2:
#             if i + 1 == len(boards):
#                 answer+='BB'
#                 break
#             else:
#                 if boards[i+1]!='X':
#                     answer+='BB'
#                     temp=0
#     elif boards[i]=='.':
#         if temp==0:
#             answer+='.'
#             temp=0
#         else:
#             check=1
# if check==0:
#     if answer=='' or answer=='.':
#         print(-1)
#     else:
#         print(answer)
# else:
#     print(-1)
board = input()
board = board.replace('XXXX',"AAAA")
board = board.replace("XX","BB")
if 'X' in board:
    print(-1)
else:
    print(board)