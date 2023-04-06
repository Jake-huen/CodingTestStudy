trie = {}
n = int(input())
for _ in range(n):
    dirs = input().split("\\")
    cur_dir = trie
    for dir in dirs:
        if dir not in cur_dir:
            cur_dir[dir] = {}
        cur_dir = cur_dir[dir]
    cur_dir['*'] = 'End'
def rec_print(trie, space_num):
    for word in sorted(trie):
        if word != '*':
            print(' ' * space_num + word)
            rec_print(trie[word], space_num + 1)
rec_print(trie, 0)
