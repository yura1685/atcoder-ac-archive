mod = 998244353
K = int(input())
C = list(map(int, input().split()))

fac = [1] * (K + 1)
for i in range(1, K+1):
    fac[i] = fac[i-1] * i % mod
inv = [1] * (K + 1)
inv[K] = pow(fac[-1], -1, mod)
for i in range(K-1, -1, -1):
    inv[i] = inv[i+1] * (i + 1) % mod

def time(A, B):
    N = min(K + 1, len(A) + len(B) - 1)
    res = [0] * N
    for i in range(N):
        x = 0
        for j in range(i+1):
            if j < len(A) and i-j < len(B):
                x += A[j] * B[i-j]
                x %= mod
        res[i] = x
    return res

f = [1]
for c in C: f = time(f, inv[:c+1])

ans = 0
for i in range(len(f)):
    ans += fac[i] * f[i]
    ans %= mod

print(ans - 1 if ans else mod - 1)