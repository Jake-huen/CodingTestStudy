arr = [1, 66, 12, 4, 63, 72]


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


print(arr)
print("버블 sort 실행")
bubblesort(arr)
print(arr)
