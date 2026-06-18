from functools import cache

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
K = int(input())
print(fib(K),fib(K+1))