from itertools import accumulate
from more_itertools import run_length
from sys import setrecursionlimit
from functools import cache

setrecursionlimit(10**8)

N = int(input())
mod = 10**9 + 7
T = [int(input()) for _ in range(N)]
T.sort()
X = list(accumulate(T))
Y = list(run_length.encode(T))

@cache
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1) % mod
    
print(sum(X))

pat = 1
for _, e in Y:
    if e == 1:
        continue
    pat = (pat*f(e)) % mod

print(pat)