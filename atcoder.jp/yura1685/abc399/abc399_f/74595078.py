N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
fact = [1] * (K+1)
inv = [1] * (K+1)
for i in range(1, K+1):
    fact[i] = fact[i-1] * i % mod
    inv[i] = pow(fact[i], -1, mod)
X = [1] + [0] * K
s, t = 0, 0
for a in A:
    s = (s + a) % mod
    Y = [0] * (K+1)
    p = 1
    for j in range(K+1):
        Y[j] = p * inv[j] % mod
        p = p * s % mod
    c = 0
    for j in range(K+1):
        c = (c + Y[j] * X[K-j]) % mod
    t = (t + c) % mod
    m = (mod - s) % mod
    pm = 1
    for j in range(K+1):
        term = pm * inv[j] % mod
        X[j] = (X[j] + term) % mod
        pm = pm * m % mod

print(t * fact[K] % mod) 