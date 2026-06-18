from collections import defaultdict
from functools import cache
mod = 10 ** 9 + 7
N, M = map(int,input().split())
X = M
d = defaultdict(int)
for p in range(2,M+1):
    if X == 1: break
    if p*p > M:
        d[X] += 1
        break
    while X % p == 0:
        X //= p
        d[p] += 1

@cache
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1) % mod

for i in range(N+50):
    fact(i)

def comb(n,k):
    k = min(n,k)
    up = fact(n)
    do = fact(n-k) * fact(k) % mod
    return up * pow(do, mod-2, mod) % mod

ans = 1
for e in d.values():
    ans *= comb(N-1+e,e)
    ans %= mod
print(ans % mod)