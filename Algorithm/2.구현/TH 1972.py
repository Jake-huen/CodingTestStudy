while True:
    s = input()
    if s=='*':
        break
    for d in range(1,len(s)-1):
        check=set()
        for i in range(len(s)-d):
            pairs = s[i]+s[i+d]
            if pairs in check:
                print(f"{s} is NOT surprising.")
                break
            else:
                check.add(pairs)
        else:
            continue
        break
    else:
        print(f"{s} is surprising.")