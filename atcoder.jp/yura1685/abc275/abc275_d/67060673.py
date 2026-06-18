from sys import setrecursionlimit
from functools import cache

N = int(input())

@cache
def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)

print(f(N))