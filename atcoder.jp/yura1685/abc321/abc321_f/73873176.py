Q, K = map(int, input().split())
mod = 998244353
coeffs = [1] + [0] * K

def kakezan(F, a):
    for i in range(K, a-1, -1):
        F[i] += F[i-a]
        F[i] %= mod

def warizan(F, a):
    for i in range(a, K+1):
        F[i] += (mod - F[i-a])
        F[i] %= mod

for _ in range(Q):
    q, n = input().split()
    n = int(n)
    if q == '+':
        kakezan(coeffs, n)
    else:
        warizan(coeffs, n)
    print(coeffs[K])