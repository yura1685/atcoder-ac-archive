N, M = map(int, input().split())
mod = 998244353

fact = [1]
for i in range(1, N+1):
    fact.append(fact[-1] * i % mod)
rev = [-1] * N + [pow(fact[-1], -1, mod)]
for i in range(N-1, -1, -1):
    rev[i] = rev[i+1] * (i+1) % mod

def perm(n, k): return fact[n] * rev[n-k] % mod if n >= k else 0

C = [0] * M
for i in range(1,N+1): C[i%M] += 1

ans = [0]
for k in range(1, N+1):
    p = 1
    for i in range(M):
        p = p * perm(k, C[i]) % mod
    ans.append(p)

A = [ans[j] * rev[j] % mod for j in range(N+1)]

for k in range(1, N+1):
    a = 0
    for j in range(1, k+1):
        term = A[j] * rev[k-j] % mod
        if (k-j) % 2 == 1:
            a = (a - term) % mod
        else:
            a = (a + term) % mod
    print(a % mod)