from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10**9)

N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
mod = 10**9+7


@cache
def g(n):
    if n == 0:
        return 1
    else:
        return n*g(n-1) % mod
    


@cache
def f(a,b):
    bunsi, bunbo = g(a), g(a-b)*g(b)
    return bunsi*pow(bunbo,mod-2,mod)%mod

M, m = 0, 0
for i in range(N):
    if K <= i+1:
        M += A[i]*f(i,K-1)
        M %= mod
    if i <= N-K:
        m += A[i]*f(N-i-1,K-1)
        m %= mod
print((M-m)%mod)