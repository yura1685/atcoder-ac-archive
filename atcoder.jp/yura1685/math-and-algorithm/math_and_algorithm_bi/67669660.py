from sys import setrecursionlimit
from functools import cache
setrecursionlimit(10**8)

N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7

@cache
def f(n):
    if n == 0:
        return 1
    return n*f(n-1) % mod

def comb(n,k):
    return f(n)*pow(f(n-k),mod-2,mod)*pow(f(k),mod-2,mod)

ans = 0
for i in range(N):
    x = min(i,N-i-1)
    ans += A[i]*comb(N-1,i)
    ans %= mod

print(ans)