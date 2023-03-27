# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
answer = [0, 0]
def check(x, y, idx,arr):
    temp = arr[x][y]
    for i in range(x, x + idx):
        for j in range(y, y + idx):
            if arr[i][j] != temp:
                idx = idx // 2
                check(x, y, idx,arr)
                check(x, y + idx, idx,arr)
                check(x + idx, y, idx,arr)
                check(x + idx, y + idx, idx,arr)
                return
    answer[temp] += 1
def solution(arr):
    
    length = len(arr)
    
    check(0, 0, length,arr)
    return answer