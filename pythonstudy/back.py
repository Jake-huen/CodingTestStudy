def solution(low, high, img):
    answer = 0
    # len(img) -> 세로 개수, len(img[0]) -> 가로 개수
    for i in range(len(img)):
        for j in range(len(img[0])):
            garo=1
            sero=1
            if img[i][j]=='#': #왼쪽 상단 모서리가 #인 경우
                if img[i+sero][j]=='#':
                    while img[i+sero][j]!='.':
                        sero+=1
                    garo=1
                    if img[i][j+garo]=='#':
                        while img[i][j+garo]!='.':
                            garo+=1
                        bottom_garo=0
                        for k in range(1,garo+1):
                            if img[i+sero-1][j+k]=='#':
                                bottom_garo+=1
                        if bottom_garo!=garo:
                            break
                        else:
                            right_sero=0
                            for k in range(1,sero+1):
                                if img[i+k][j+garo-1]=='#':
                                    right_sero+=1
                            if right_sero!=sero:
                                break
            if garo!=1 and sero!=1:
                count=0
                for x in range(i+1,sero):
                    for y in range(j+1,garo):
                        if img[x][y]=='#':
                            count+=1
                check = (count/((garo-1)*(sero-1)-2)*((garo-1)*(sero-1)-2))*100
                if check>=low and check<high:
                    answer+=1
    return answer
solution(3,4,['######','#.###.#','#####'])