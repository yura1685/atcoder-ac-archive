N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

fact = [1] * (K+1)
for i in range(1, K+1):
    fact[i] = fact[i-1] * i % mod
inv = [1] * (K+1)
inv[K] = pow(fact[K], -1, mod)
for i in range(K-1, -1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

f = [0] * (K+1)
f[0] = N
pa = A.copy()

for k in range(1, K+1):
    s = 0
    for i in range(N):
        s += pa[i]
        pa[i] = pa[i] * A[i] % mod
        if s > mod: s %= mod
    s = s * inv[k] % mod
    f[k] = s

sum_2A = [0] * (K+1)
pa2 = [2 * a % mod for a in A ]

for X in range(1, K + 1):
    s2 = 0
    for i in range(N):
        s2 += pa2[i]
        pa2[i] = pa2[i] * (2 * A[i]) % mod
    sum_2A[X] = s2 % mod

for X in range(1, K+1):
    ans = 0
    for k in range(X+1):
        ans += f[X-k] * f[k] % mod
    ans = ans * fact[X] % mod
    ans -= sum_2A[X]
    ans = ans * inv[2] % mod
    print(ans)