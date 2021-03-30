n=int(input())

def pactorial(number):
    if number==0 or number==1:
        return 1
    return pactorial(number-1)*number
print(pactorial(n))
