X, Y, Z = map(int, input().split())
N = X + Y + Z
mod = 998244353
ans = 0
fact = [1] * (N+2)
inv = [1] * (N+2)
for i in range(1, N+2):
    fact[i] = fact[i-1] * i % mod
inv[-1] = pow(fact[-1], -1, mod)
for i in range(N, -1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

def comb(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * inv[n-k] * inv[k] % mod

for m in range(1, min(X, Z) + 1):
    k1 = 2*m - 1
    k2 = 2*m
    w1 = 2 * comb(X-1, m-1) * comb(Z-1, m-1) % mod
    w2 = (comb(X-1, m) * comb(Z-1, m-1) + comb(X-1, m-1) * comb(Z-1, m)) % mod
    ans += w2 * comb(N-k2, Y-k2) + w1 * comb(N-k1, Y-k1)
    ans %= mod

print(ans)