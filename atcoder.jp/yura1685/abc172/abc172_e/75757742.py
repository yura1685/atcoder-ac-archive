N, M = map(int, input().split())

mod = 10 ** 9 + 7

fact = [1, 1]
for i in range(2, M+1):
    fact.append(fact[-1] * i % mod)
rev = [-1] * M + [pow(fact[-1], -1, mod)]
for i in range(M-1, -1, -1):
    rev[i] = rev[i+1] * (i+1) % mod

def comb(n, k):
    return fact[n] * rev[n-k] * rev[k] % mod

def perm(n, k):
    return fact[n] * rev[n-k] % mod

ans = 0
for k in range(0, N+1):
    ans += perm(M-k, N-k) * comb(N, k) * (1 - 2 * (k % 2)) % mod

ans = ans * perm(M, N) % mod
print(ans)