n = input()
i = 0


def check():
    i = 0
    while i < len(n):
        if n[i] == '1':
            i += 2
            # print("i+=2", i)
            if i < len(n):
                if n[i] == '0' and n[i - 1] == '0':
                    while i < len(n) and n[i] == '0':
                        i += 1
                        # print("0: i+=1", i)
                    if i<len(n):
                        if n[i] == '1':
                            while i < len(n) and n[i] == '1':
                                i += 1
                                # print("1: i+=1", i)
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif n[i] == '0':
            i += 1
            # print("01: i+=1", i)
            if i < len(n):
                if n[i] == '1':
                    i += 1
                    continue
                else:
                    return False
            else:
                return False
    return True


if check():
    print("SUBMARINE")
else:
    print("NOISE")
