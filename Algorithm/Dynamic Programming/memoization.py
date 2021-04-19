def fib_memo(n, cache):
    # 코드를 작성하세요.
    if cache[n]!=0:
        return cache[n]
    else:
        return fib_memo(n-1,cache)+fib_memo(n-2,cache)
def fib(n):
    fib_cache = [0]*100001
    fib_cache[1]=1
    fib_cache[2]=1
    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))