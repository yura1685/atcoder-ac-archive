mod = 998244353

N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

M = max(D)
inv = [1] * (M + 1)
fact = 1
for i in range(1, M+1):
    fact = fact * i % mod
inv[M] = pow(fact, -1, mod)
for i in range(M-1, -1, -1):
    inv[i] = inv[i+1] * (i + 1) % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    res = 1
    for i in range(r):
        res = (res * (n - i)) % mod
    return res * inv[r] % mod

g = [[] for _ in range(N)]
for i in range(N - 1):
    p = P[i] - 1
    g[p].append(i + 1)

t = [0]
for u in t:
    for v in g[u]:
        t.append(v)

SC = C.copy()
SD = D.copy()

for u in t[::-1]:
    if u:
        p = P[u-1] - 1
        SC[p] += SC[u]
        SD[p] += SD[u]

ans = 1
for u in range(N):
    if SC[u] < SD[u]:
        exit(print(0))
    pick = SC[u] - SD[u] + D[u]
    ans = ans * comb(pick, D[u]) % mod

print(ans)