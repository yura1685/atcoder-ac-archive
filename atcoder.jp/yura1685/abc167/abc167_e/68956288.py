from functools import cache

N, M, K = map(int,input().split())
mod = 998244353

@cache
def comb(n,k):
    if k == 0:
        return 1
    return (comb(n,k-1) * (n-k+1)) * pow(k,mod-2,mod) % mod

ans = 0
for i in range(K+1):
    ans += M * pow(M-1,N-i-1,mod) * comb(N-1,i)
    ans %= mod

print(ans)