from functools import cache

@cache
def f(n):
    res = 1
    for i in range(2,n+1):
        res = res * i % mod
    return res

def comb(n,k):
    return f(n)*pow(f(n-k)*f(k),mod-2,mod) % mod

N, K = map(int, input().split())
mod = 10**9 + 7

for i in range(1,K+1):
    if i > N-K+1:
        print(0)
    else:
        print(comb(N-K+1, i) * comb(K-1, i-1) % mod)
