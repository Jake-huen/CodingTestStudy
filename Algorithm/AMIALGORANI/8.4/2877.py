k = int(input())
temp = bin(k+1)[3:]
ans = ""
for i in range(len(temp)):
    if temp[i] == "0":
        ans+='4'
    else:
        ans+='7'
print(ans)

