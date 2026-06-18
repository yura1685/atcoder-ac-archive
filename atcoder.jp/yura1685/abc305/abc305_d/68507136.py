from functools import cache
from sys import setrecursionlimit
from bisect import *

setrecursionlimit(10**8)

N = int(input())
A = list(map(int,input().split()))

@cache
def f(t):
    if t == 0:
        return 0
    l, r = bisect_left(A,t), bisect(A,t)
    if l == r:
        if l % 2 == 1:
            return f(A[l-1])
        else:
            return f(A[l-1]) + t - A[l-1]
    else:
        if l % 2 == 0:
            return f(A[l-1]) + t - A[l-1]
        else:
            return f(A[l-1])
        
Q = int(input())
for _ in range(Q):
    L, R = map(int,input().split())
    print(f(R) - f(L))