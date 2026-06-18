import functools

@functools.cache
def f(x):
    if x == 1:
        return 0
    a = f(x//2)
    b = f((x+1)//2)
    return x + a + b

N = int(input())
print(f(N))