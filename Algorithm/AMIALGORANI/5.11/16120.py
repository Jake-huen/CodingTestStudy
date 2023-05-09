n = input()
x = n.replace("PPAP", "P")
if x == "P" or x == "PPAP":
    print("PPAP")
else:
    x = x.replace("PPAP", "P")
    if "A" in x:
        print("NP")
    else:
        print("PPAP")
