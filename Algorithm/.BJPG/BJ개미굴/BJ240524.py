def add(dict, arr):
    if len(arr) == 0:
        return
    if arr[0] not in dict:
        dict[arr[0]] = {}
    add(dict[arr[0]], arr[1:])


def _print(dict, l):
    for key in sorted(dict.keys()):
        print("--" * l + key)
        _print(dict[key], l + 1)


dict = {}
n = int(input())
for _ in range(n):
    temp = list(input().split(" "))
    add(dict, temp[1:])
_print(dict, 0)
