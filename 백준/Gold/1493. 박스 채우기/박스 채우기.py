import sys
input = sys.stdin.readline

length, width, height = map(int,input().split()) # length, width, height
box=length*width*height
n = int(input()) # 세준이가 가지는 큐브의 개수
cube=[]
for _ in range(n):
    cube.append(list(map(int,input().split())))
cube.sort(reverse=True)

answer=0
total_now=0
for c_idx, c_cnt in cube:
    total_now = total_now*8
    c_len = 2 ** c_idx

    put_cube = (length//c_len)*(width//c_len)*(height//c_len)
    put_cube = put_cube-total_now
    if put_cube>c_cnt: # 가지고있는 큐브의 개수보다 많으면
        put_cube = c_cnt

    answer += put_cube
    total_now += put_cube

if total_now == box: #부피
    print(answer)
else:
    print(-1)




# 젤 작은거로 모두...?
# for i in range(3):
#     box_length = box[i]
#     count=0
#     for index,(key,elem) in enumerate(cube.items()):
#         # print(index,key,elem)
#         if box_length%key==0 or cube[key]<=box_length/key == 0: # 변의 길이를 큐브 길이로 나눈게
#             break
#         else:
#             box_length=box_length%key
#             count += box_length / key



